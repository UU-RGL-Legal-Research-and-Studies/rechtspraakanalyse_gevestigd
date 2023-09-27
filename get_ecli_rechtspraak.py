import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Setup webdriver
s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)

# Navigate to webpage
driver.get('https://uitspraken.rechtspraak.nl/#!/resultaat?zoekterm=affectieschade&inhoudsindicatie=zt0&sort=Relevance&publicatiestatus=ps1&uitspraakdatumrange=na&uitspraakdatuma=01-01-2019&rechtsgebied=r3')

wait = WebDriverWait(driver, 10)

while True:
    try:
        # Wacht tot de 'Laad meer resultaten' knop zichtbaar is en klik erop
        load_more_button = wait.until(EC.visibility_of_element_located((By.ID, 'lib-rnl-lib-rnl-laadMeerBtn')))
        load_more_button.click()

        # Optionele pauze om te zorgen dat de pagina volledig is geladen
        driver.implicitly_wait(5)
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


time.sleep(300)