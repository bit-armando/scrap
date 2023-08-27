from selenium import webdriver
from selenium.webdriver.common.by import By  # Busqueda mediante xpath
from webdriver_manager.chrome import ChromeDriverManager # Busca el driver mas reciente para nuestro navegador
from time import sleep

proxy = webdriver.Proxy()
proxy.proxy_type = webdriver.common.proxy.ProxyType.MANUAL
proxy.http_proxy = '37.19.220.179:8443' # http://free-proxy.cz/es/

# Paso 1: instanciar un driver en el navegador
options = webdriver.ChromeOptions()
options.add_argument('--proxy-server=http://37.19.220.179:8443')
# options.add_argument('--incognito')
# options.add_argument('--headless')

# Descargue el controlador de acuerdo a laversiónde chrome que tengo instalado
driver = webdriver.Chrome(ChromeDriverManager().install(),options=options)
# Paso **: Hacer que el navegador cargue la página web
driver.get("https://ekilu.com/es/recetas/hamburguesas")
sleep(120)
driver.close()