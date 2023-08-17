import requests
import pandas as pd
import numpy as np
import re
from bs4 import BeautifulSoup
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

base_url = "https://www.quelibroleo.com/mejores-quelibroleo?sort=&page="
pages = 10

def GetDataBook(link:str):
    datos_libro  = requests.get(link).text
    librosoup = BeautifulSoup(datos_libro, 'html5lib')
    try:
        li = librosoup.find("div", {"class": "card-block"}).find_all('li')

        genero = li[0].find('a').text
        editorial = li[1].find('a').text
        año = li[2].text.replace('Año de edición','')

        return genero,editorial,año
    except:
        return np.nan,np.nan,np.nan




libros_data = pd.DataFrame(columns=["Titulo",
"Autor",
"NotaMedia",
"Rango", 
"NumVotos",
"NumCriticas",
"Genero",
"Editorial",
"AñoEdicion",
"Resumen"])

print("Iniciando scrape")
for page in range(1, pages+1):
    url = f"{base_url}{page}"
    data  = requests.get(url).text

    soup = BeautifulSoup(data, 'html5lib')

    for libro in soup.find_all("div", {"class": "item"}):
        Titulo=libro.find('span').text
        Autor=libro.find('div', class_='col-lg-8 col-xs-12').find('small').text
        NotaMedia=libro.find("div", {"class": "estadisticas"}).find("span").text.strip()
        Rango=libro.find("i", {"class": "puntuacion"}).text.strip()

        NumVotos=libro.find("i", {"class": "numero_votos"}).text.strip()
        NumVotos=re.sub(r'[\t\n votos]', '', NumVotos)

        NumCriticas=libro.find("i", {"class": "numero_criticas"}).text.strip()
        NumCriticas = re.sub(r'[\t\n críticas]', '', NumCriticas)

        link = libro.find('a')["href"]
        
        Genero,Editorial,AñoEdicion = GetDataBook(link)
        Resumen=libro.find('div', class_='text').find('p').text



        libros_data = libros_data.append({"Titulo":Titulo,
        "Autor":Autor,
        "NotaMedia":NotaMedia,
        "Rango":Rango,
        "NumVotos":NumVotos,
        "NumCriticas":NumCriticas,
        "Genero":Genero,
        "Editorial":Editorial,
        "AñoEdicion":AñoEdicion,
        "Resumen":Resumen
        }, ignore_index=True)
    print('pagina ',page,' obtenida')


libros_data.to_csv("MejoresLibros.csv")
