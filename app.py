from flask import Flask, render_template, request, send_file, session, redirect, url_for
import requests
import xml.etree.ElementTree as ET
import pandas as pd
from io import BytesIO
import tempfile
from ECLI_affectieschade1 import unique_list
import pickle
import shutil
import os
import time
import re
# from ratelimit import limits, sleep_and_retry

app = Flask(__name__)
app.secret_key = 'hello_world'

# Maximum requests per minute (to reduce pressure on API-server)
# MAX_REQUESTS = 50 
# ONE_MINUTE = 60

# # Sample ECLIs
ECLIs = unique_list #list from other file where ECLIs have been subtracted (using Webparsing)
ECLIs.sort(reverse=True)
ECLI_texts = {} # ECLI_texts[ecli] = {'texts': [], 'current_index': 0}
ECLI_cache = {}  # Cache for XML roots

def highlight_term(text, term):
    #return text.replace(term, term)
    return text.replace(term, f'<span class="highlight">{term}</span>')

# @sleep_and_retry
# @limits(calls=MAX_REQUESTS, period=ONE_MINUTE)
def api_request(ecli):
    identifier_link = None
    namespaces = {
        'rdf': "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
        'dcterms': "http://purl.org/dc/terms/",
    }

    if ecli in ECLI_cache:
        temp_file_name = ECLI_cache[ecli]
        with open(temp_file_name, 'rb') as file:
            root = ET.parse(file).getroot()
    else:
        url = f"https://data.rechtspraak.nl/uitspraken/content?id={ecli}"
        response = requests.get(url, stream=True)
        with tempfile.NamedTemporaryFile(delete=False, suffix='.xml') as temp_file:
            shutil.copyfileobj(response.raw, temp_file)
            temp_file_name = temp_file.name

        ECLI_cache[ecli] = temp_file_name
        with open(temp_file_name, 'rb') as file:
            root = ET.parse(file).getroot()
        time.sleep(3)

    # Zoek naar alle dcterms:identifier tags
    for identifier_tag in root.findall('.//rdf:Description/dcterms:identifier', namespaces):
        if identifier_tag.text and identifier_tag.text.startswith('http'):
            identifier_link = identifier_tag.text
            break

    return root, identifier_link


@app.route('/', methods=['GET', 'POST'])
def index():
    global ECLI_texts  # Declare ECLI_texts as global

    search_results_count = 0  # Initialize search results count

    if request.method == 'POST':
        # Verkrijg ruwe zoektermen van de gebruiker
        raw_search_terms = request.form.get('search_terms').split(',')
        # Verwerk de ruwe zoektermen om een lijst van lijsten te maken,
        # waar elke lijst synoniemen bevat die door de gebruiker zijn ingevoerd
        search_terms = [term.split('|') for term in raw_search_terms]
        
        ECLI_texts = {}
        for ecli in ECLIs:
            root, identifier_link = api_request(ecli)
            # Verzamel alle teksten die voldoen aan de zoekcriteria
            texts = [elem.text for elem in root.iter() if elem.text and all(
                any(synonym.lower() in elem.text.lower() for synonym in term)
                for term in search_terms
            )]
            # Voeg de gemarkeerde tekst toe
            highlighted_texts = []
            for text in texts:
                for term_group in search_terms:
                    for synonym in term_group:
                        text = highlight_term(text, synonym)
                highlighted_texts.append(text)
            ECLI_texts[ecli] = {'texts': highlighted_texts, 'identifier_link':identifier_link, 'current_index': 0}
            search_results_count += len(highlighted_texts)  # Update search results count
    update_excel_file()
    return render_template('index.html', ECLI_texts=ECLI_texts, search_results_count=search_results_count)

def remove_html_tags(text):
    """Verwijder HTML-tags uit een string"""
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)

def update_excel_file():
    # Maak een lijst van tuples voor elke rij in de DataFrame
    data = []
    for ecli, texts in ECLI_texts.items():
        # Verwijder HTML-tags uit de tekst
        result_text = remove_html_tags(texts['texts'][ECLI_texts[ecli]['current_index']]) if texts['texts'] else 'none'
        
        # Haal de link op uit de dictionary
        link = texts.get('identifier_link', 'No link available')

        # Voeg de gegevens toe aan de lijst
        data.append((ecli, link, result_text))

    # Maak een DataFrame van de lijst
    df = pd.DataFrame(data, columns=['ECLI', 'Link', 'Result'])

    # Sla de DataFrame op als Excel-bestand
    with tempfile.NamedTemporaryFile(delete=False, suffix='.xlsx') as temp_file:
        df.to_excel(temp_file, index=False)

    # Sla het pad naar het Excel-bestand op in de sessie
    session['temp_excel_file'] = temp_file.name
    session.modified = True


# Voeg ergens in je code een functie toe om het 'vorige' en 'volgende' element te krijgen
def get_sibling_elements(ecli, index):
    root = api_request(ecli)
    current_elem = root.find(f".//*[@index='{index}']")
    prev_elem = current_elem.getprevious() if current_elem is not None else None
    next_elem = current_elem.getnext() if current_elem is not None else None
    return prev_elem, next_elem

@app.route('/previous/<ecli>', methods=['GET'])
def previous(ecli):
    if ecli in ECLI_texts:
        ECLI_texts[ecli]['current_index'] = max(0, ECLI_texts[ecli]['current_index'] - 1)
    update_excel_file()
    return redirect(url_for('index'))

@app.route('/next/<ecli>', methods=['GET'])
def next(ecli):
    if ecli in ECLI_texts:
        ECLI_texts[ecli]['current_index'] = min(len(ECLI_texts[ecli]['texts']) - 1, ECLI_texts[ecli]['current_index'] + 1)
    update_excel_file()
    return redirect(url_for('index'))

@app.route('/delete/<ecli>', methods=['GET'])
def delete(ecli):
    if ecli in ECLI_texts:
        del ECLI_texts[ecli]['texts'][ECLI_texts[ecli]['current_index']]
        ECLI_texts[ecli]['texts'] = [text for text in ECLI_texts[ecli]['texts'] if text]  # remove any empty strings which may occur due to deletion
    update_excel_file()
    return redirect(url_for('index'))

@app.route('/download/excel', methods=['GET'])
def download_excel():
    temp_excel_file = session.get('temp_excel_file', None)
    if temp_excel_file:
        return send_file(
            temp_excel_file,
            as_attachment=True,
            download_name='ECLI_results.xlsx',
            mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        )
    else:
        return "No Excel file generated", 404

# Vergeet niet om de tijdelijke bestanden op te ruimen wanneer u klaar bent!
for temp_file_path in ECLI_cache.values():
    os.remove(temp_file_path)

if __name__ == '__main__':
    app.run(debug=True)
