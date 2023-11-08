#Note: always check /robots.txt at the end of the url before webscraping. This to see whether scraping is permitted

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Setup webdriver
s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)

# Navigate to webpage
driver.get('https://uitspraken.rechtspraak.nl/#!/resultaat?zoekterm=affectieschade&inhoudsindicatie=zt0&sort=Relevance&publicatiestatus=ps1&uitspraakdatumrange=tussen&uitspraakdatuma=01-01-2019&uitspraakdatumb=31-10-2023&rechtsgebied=r3')
wait = WebDriverWait(driver, 5)

while True:
    try:
        # Wacht tot de 'Laad meer resultaten' knop interacteerbaar is
        load_more_button = wait.until(EC.element_to_be_clickable((By.ID, 'lib-rnl-lib-rnl-laadMeerBtn')))
        
        # Gebruik JavaScript om op de knop te klikken
        driver.execute_script("arguments[0].click();", load_more_button)

        # Wacht tot de nieuwe resultaten zijn geladen
        time.sleep(5)  # Pas de slaaptijd aan indien nodig voor jouw verbinding en de snelheid van de website
    except Exception as e:
        print("Kan niet meer resultaten laden of er is een andere fout opgetreden:", e)
        break

elements = driver.find_elements(By.XPATH, '//a[contains(@href, "ECLI:NL")]')

elements_list = []
# Loop door elk element en print de tekst
for element in elements:
    elements_list.append(element.text)

# Maak een lege lijst aan om de gesplitste teksten in op te slaan
split_texts = []

# Loop door elk element in element_list en split bij de eerste spatie
for text in elements_list:
    first_part = text.split(' ', 1)[0]
    split_texts.append(first_part)

# Print de inhoud van de nieuwe lijst
print(len(split_texts))
print(split_texts)

# Sluit de browser na 5 seconden
time.sleep(5)
driver.quit()
