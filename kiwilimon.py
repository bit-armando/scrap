from selenium.webdriver.common.by import By
import pandas as pd

from driver_selenium.driver_chrome import init_driver

driver = init_driver()

url = "https://www.kiwilimon.com/recetas/desayunos"
driver.get(url)

# Obtener recetas de la pagina con iteraciones
for i in range(10):
    try:
        nextpage = driver.find_element(By.XPATH, '//div[@class="recipelist-btn-next"]')
        nextpage.click()
    except:
        pass

recetas_items = driver.find_elements(By.XPATH, '//div[@class="searchlist-muestra tools feed-receta-ficha"]/a')


# Sacar datos de las recetas individuales e incluirlos en un DataFrame
receta = init_driver()
df = pd.DataFrame(columns=[
    'nombre',#
    'categoria', #
    'tiempo',#
    'dificultad',#
    'porciones',#
    'ingredientes',#
    'pasos',#
    'img',#
])


for item in recetas_items:
    receta.get(item.get_attribute('href'))
    
    try:
        paywall = receta.find_element(By.XPATH, '//div[@id="paywall-registro"]')
    except:
        paywall = None
    
    # Se puede agregar una categoria con paywall para las recetas premium
    if True:
        nueva_receta = []
        
        try:
            nombre = receta.find_element(By.ID, 'nombre-receta').text
        except:
            nombre = None
        
        try:
            tiempo = receta.find_element(By.XPATH, '//div[@class="icon-k7-receta-tcocinar"]/span').text
        except:
            tiempo = None
        
        try:
            dificultad = receta.find_element(By.XPATH, '//div[@class="icon-k7-receta-tdificultad"]/span').text
        except:
            dificultad = None
            
        try:
            porciones = int(receta.find_element(By.XPATH, '//*[@id="recipe"]/div[3]/div[1]/div[1]/div[3]/span').text)
        except:
            porciones = None

        try:
            ingredientes_items = receta.find_elements(By.XPATH, '//div[@id="ingredients-original"]/label')
            ingredientes = []
            for item in ingredientes_items:
                ingredientes.append(item.text)
        except:
            ingredientes = None
        
        try:
            pasos_items = receta.find_elements(By.XPATH, '//div[@class="recipe-intro-data-pasos-normal"]/label')
            pasos = []
            for item in pasos_items:
                pasos.append(item.text)
        except:
            pasos = None

        try:
            categoria = receta.current_url.split('/')
            categoria = categoria[4]
        except:
            categoria = None
            
        try:
            img = receta.find_element(By.XPATH, '//div[@class="video receta-normal"]/img')
            img = img.get_attribute('src')
        except:
            img = None
        
        nueva_receta.append(nombre)
        nueva_receta.append(categoria)
        nueva_receta.append(tiempo)
        nueva_receta.append(dificultad)
        nueva_receta.append(porciones)
        nueva_receta.append(ingredientes)
        nueva_receta.append(pasos)
        nueva_receta.append(img)
        
        
        df.loc[len(df)] = nueva_receta
    else:
        pass

receta.close()    
driver.close()

# Guardar DataFrame en un archivo csv
df.to_csv('recetas.csv', index=False)
print(df.head())
print(df.tail())