# Análisis de géneros más valorados en QueLibroLeo.

Este proyecto tiene como objetivo analizar los méjores géneros literarios.

## Índice

1. [Introducción](#introducción)
2. [Estructura](#estructura)
3. [Resultados](#resultados)

## Introducción

Si decidiese escribir un libro, ¿Qué género tendría más éxito?. Para responder esta pregunta, y dejando de lado gustos individuales, se ha creado este proyecto. Personalmente, una de las web por las que me guio a la hora de elegir mi próxima lectura es la web [Quelibroleo](https://quelibroleo.com/). 
Ya que quiero saber qué género o que tipo de libros tienen más éxito, se ha hecho scraping sobre el ranking de mejores libros, dejando de lado el resto de rankings.

## Estructura

Se puede dividir el proyecto en dos partes diferenciadas. La primera es la obtención de los datos, que se han extraido usando el script de python [web_scraping.py](src/web_scraping.py) utilizando la librería [beautifulsoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/), y guardando los datos extraidos en un dataframe. 

La segunda parte del proyecto es el análisis en sí, que se puede encontrar en el archivo [analisis.ipynb](notebooks/analisis.ipynb)

## Resultados

