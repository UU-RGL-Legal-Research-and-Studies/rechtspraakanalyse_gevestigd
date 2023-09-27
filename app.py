from flask import Flask, render_template, request, send_file, session, redirect, url_for
import requests
import xml.etree.ElementTree as ET
import pandas as pd
from io import BytesIO
import tempfile
from ECLI_affectieschade1 import unique_list
import pickle

app = Flask(__name__)
app.secret_key = 'hello_world'

# # Sample ECLIs
ECLIs = unique_list #list from other file where ECLIs have been subtracted (using Webparsing)
ECLIs.sort(reverse=True)
ECLI_texts = {} # ECLI_texts[ecli] = {'texts': [], 'current_index': 0}
ECLI_cache = {}  # Cache for XML roots

def api_request(ecli):
    if ecli in ECLI_cache:
        return ECLI_cache[ecli]

    # Uncomment this section when you run the code

    url = f"https://data.rechtspraak.nl/uitspraken/content?id={ecli}"
    response = requests.get(url)
    root = ET.fromstring(response.content)
        
    ECLI_cache[ecli] = root
    return root

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
            root = api_request(ecli)
            # Verzamel alle teksten die voldoen aan de zoekcriteria
            texts = [elem.text for elem in root.iter() if elem.text and all(
                any(synonym.lower() in elem.text.lower() for synonym in term)
                for term in search_terms
            )]
            ECLI_texts[ecli] = {'texts': texts, 'current_index': 0}
            search_results_count += len(texts)  # Update search results count

    return render_template('index.html', ECLI_texts=ECLI_texts, search_results_count=search_results_count)

def update_excel_file():
    df = pd.DataFrame([(ecli, texts['texts'][ECLI_texts[ecli]['current_index']] if texts['texts'] else 'none') 
                       for ecli, texts in ECLI_texts.items()], columns=['ECLI', 'Result'])

    with tempfile.NamedTemporaryFile(delete=False, suffix='.xlsx') as temp_file:
        df.to_excel(temp_file, index=False)

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
        ECLI_texts[ecli]['texts'][ECLI_texts[ecli]['current_index']] = 'No result'
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

if __name__ == '__main__':
    app.run(debug=True)