from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager # Busca el driver mas reciente para nuestro navegador

def init_driver():
    options = webdriver.ChromeOptions()
    # options.add_argument('--incognito')
    # options.add_argument('--headless')

    # Descargue el controlador de acuerdo a laversiónde chrome que tengo instalado
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options)
    return driver