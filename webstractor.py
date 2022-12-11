
## paquetes necesarios 

import pandas as pd
import numpy as np
import selenium
import re

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


## cargar servicio

## cargar el servicio
service = ChromeService(executable_path=ChromeDriverManager().install())

#correr el servicio
driver = webdriver.Chrome(service = service)


##función extraer goles totales

def goles(pais, liga, temporada):
    url = "https://www.adamchoi.co.uk/overs/detailed"
 # cargar la url 
    driver.get(url)

    ## label 
    lapais = str("//option[@label = '%s']") % pais
    laliga = str("//option[@label = '%s']") % liga
    temp = str("//option[@label = '%s']") % temporada

    # seleccionar pais
    driver.find_element(By.XPATH,lapais).click()

    # seleccionar liga
    driver.find_element(By.XPATH, laliga).click()

    ## seleccionar temporada
    driver.find_element(By.XPATH, temp).click()

    ## seleccionar evento
    driver.find_element(By.XPATH,'//label[@analytics-event="All matches"]').click() 

    

    # partidos 
    matches = driver.find_elements(By.TAG_NAME,'tr')

    ## variables
    Fecha = []
    E_local= []
    Resultado =[]
    E_visitante = []
    
    for match in matches:
        Fecha.append(match.find_element(By.XPATH,'./td[1]').text)
        E_local.append(match.find_element(By.XPATH,'./td[2]').text)
        Resultado.append(match.find_element(By.XPATH,'./td[3]').text)
        E_visitante.append(match.find_element(By.XPATH,'./td[4]').text)   

    ## crear data.frame
    datos = pd.DataFrame({"Fecha":Fecha,"Equipo_local":E_local, 
                     "Resultado":Resultado, "E_visitante":E_visitante})

     ## liminar caracter "/"
    tempo = temporada
    tempo = str(re.sub("/", "-", tempo))

    

    ## patch 
    paths = "goles/{}_{}_{}.xlsx".format(pais, liga, tempo)

    Excel = pd.ExcelWriter(paths)

    datos.to_excel(Excel)
                 
    Excel.save()
      

## extraer corners

def corners(pais, liga, temporada):

    # url
    url = "https://www.adamchoi.co.uk/corners/detailed"

     # cargar la url 
    driver.get(url)

    ## label 
    lapais = str("//option[@label = '%s']") % pais
    laliga = str("//option[@label = '%s']") % liga
    temp = str("//option[@label = '%s']") % temporada


    # seleccionar pais
    driver.find_element(By.XPATH,lapais).click()

    # seleccionar liga
    driver.find_element(By.XPATH, laliga).click()

    ## seleccionar temporada
    driver.find_element(By.XPATH, temp).click()

    ## seleccionar evento
    driver.find_element(By.XPATH,'//label[@analytics-event="All matches"]').click() 

    

    # partidos 
    matches = driver.find_elements(By.TAG_NAME,'tr')

    ## variables
    Fecha = []
    E_local= []
    Corners =[]
    E_visitante = []
    
    for match in matches:
        Fecha.append(match.find_element(By.XPATH,'./td[1]').text)
        E_local.append(match.find_element(By.XPATH,'./td[2]').text)
        Corners.append(match.find_element(By.XPATH,'./td[3]').text)
        E_visitante.append(match.find_element(By.XPATH,'./td[4]').text)   

    ## crear data.frame
    datos = pd.DataFrame({"Fecha":Fecha,"Equipo_local":E_local, 
                     "Corners":Corners, "E_visitante":E_visitante})

    print(datos.head())

     ## liminar caracter "/"
    tempo = temporada
    tempo = str(re.sub("/", "-", tempo))

    

    ## patch 
    paths = "corners/{}_{}_{}.xlsx".format(pais, liga, tempo)

    Excel = pd.ExcelWriter(paths)

    datos.to_excel(Excel)
                 
    Excel.save()
      


def primertiempo(pais, liga, temporada):

    # url
    url = "https://www.adamchoi.co.uk/goalsbyhalf/detailed"

     # cargar la url 
    driver.get(url)

    ## label 
    lapais = str("//option[@label = '%s']") % pais
    laliga = str("//option[@label = '%s']") % liga
    temp = str("//option[@label = '%s']") % temporada

 
    # seleccionar pais
    driver.find_element(By.XPATH,lapais).click()

    # seleccionar liga
    driver.find_element(By.XPATH, laliga).click()

    ## seleccionar temporada
    driver.find_element(By.XPATH, temp).click()

    ## seleccionar evento
    driver.find_element(By.XPATH,'//label[@analytics-event="All matches"]').click() 

    

    # partidos 
    matches = driver.find_elements(By.TAG_NAME,'tr')

    ## variables
    Fecha = []
    E_local= []
    Corners =[]
    E_visitante = []
    
    for match in matches:
        Fecha.append(match.find_element(By.XPATH,'./td[1]').text)
        E_local.append(match.find_element(By.XPATH,'./td[2]').text)
        Corners.append(match.find_element(By.XPATH,'./td[3]').text)
        E_visitante.append(match.find_element(By.XPATH,'./td[4]').text)   

    ## crear data.frame
    datos = pd.DataFrame({"Fecha":Fecha,"Equipo_local":E_local, 
                     "Corners":Corners, "E_visitante":E_visitante})

    print(datos.head())


    ## liminar caracter "/"
    tempo = temporada
    tempo = str(re.sub("/", "-", tempo))

    

    ## guardar
    paths = "ptiempo/{}_{}_{}.xlsx".format(pais, liga, tempo)

    Excel = pd.ExcelWriter(paths)

    datos.to_excel(Excel)
                 
    Excel.save()


### faltas


def faltas(pais, liga, temporada):

    # url
    url = "https://www.adamchoi.co.uk/bookingpoints/detailed"

     # cargar la url 
    driver.get(url)

    ## label 
    lapais = str("//option[@label = '%s']") % pais
    laliga = str("//option[@label = '%s']") % liga
    temp = str("//option[@label = '%s']") % temporada


    # seleccionar pais
    driver.find_element(By.XPATH,lapais).click()

    # seleccionar liga
    driver.find_element(By.XPATH, laliga).click()

    ## seleccionar temporada
    driver.find_element(By.XPATH, temp).click()

    ## seleccionar evento
    driver.find_element(By.XPATH,'//label[@analytics-event="All matches"]').click() 


    # partidos 
    matches = driver.find_elements(By.TAG_NAME,'tr')

    ## variables
    Fecha = []
    E_local= []
    Corners =[]
    E_visitante = []
    
    for match in matches:
        Fecha.append(match.find_element(By.XPATH,'./td[1]').text)
        E_local.append(match.find_element(By.XPATH,'./td[2]').text)
        Corners.append(match.find_element(By.XPATH,'./td[3]').text)
        E_visitante.append(match.find_element(By.XPATH,'./td[4]').text)   

    ## crear data.frame
    datos = pd.DataFrame({"Fecha":Fecha,"Equipo_local":E_local, 
                     "Corners":Corners, "E_visitante":E_visitante})

    print(datos.head())


    ## liminar caracter "/"
    tempo = temporada
    tempo = str(re.sub("/", "-", tempo))

    

    ## guardar
    paths = "tarjetas/{}_{}_{}.xlsx".format(pais, liga, tempo)

    Excel = pd.ExcelWriter(paths)

    datos.to_excel(Excel)
                 
    Excel.save()

### ejemplos 
goles("Ukraine", "Premier League", "20/21")
goles("England", "Premier League", "22/23")

