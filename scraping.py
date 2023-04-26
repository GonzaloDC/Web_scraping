import requests
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

base_url = "https://www.quelibroleo.com/mejores-quelibroleo?sort=&page=1"
pages = 10
page_size = 10


libros_data = pd.DataFrame(columns=["Titulo",
"Autor",
"Nota Media",
"Rango", 
"NumVotos",
"NumCriticas",
"Genero",
"Editorial",
"AñoEdicion"])

for page in range(1, pages + 1):
    url = f"{base_url}/page/{page}/?sortby=post_date%3ADesc&pagesize={page_size}"
    data  = requests.get(url).text

    soup = BeautifulSoup(data, 'html5lib')

    for article in soup.find_all('article',itemprop="review"):
        ReviewBody=np.nan
        Aircraft=np.nan
        Type_Of_Traveller=np.nan
        Seat_Type=np.nan
        Route=np.nan
        Date_Flown=np.nan
        Seat_comfort=np.nan
        Cabin_Staff_Service=np.nan
        Food_Beverages=np.nan
        Inflight_Entertainment=np.nan
        Ground_Service=np.nan
        Wifi_Connectivity=np.nan
        Value_For_Money=np.nan
        Rating=np.nan
        Recommendend=np.nan
        
        Rating = article.find('span',itemprop="ratingValue").text
        ReviewBody = article.find("div", {"class": "text_content"},itemprop="reviewBody").text

        for row in article.find("tbody").find_all('tr'):

            col = row.find_all("td")

            if col[0].text == 'Aircraft':
                Aircraft=col[1].text
            if col[0].text == 'Type Of Traveller':
                Type_Of_Traveller=col[1].text
            if col[0].text == 'Seat Type':
                Seat_Type=col[1].text
            if col[0].text == 'Route':
                Route=col[1].text
            if col[0].text == 'Date Flown':
                Date_Flown=col[1].text          
            if col[0].text == 'Seat Comfort':
                Seat_comfort = col[1].find_all("span", {"class": "star fill"})[-1].text
            if col[0].text == 'Cabin Staff Service':
                Cabin_Staff_service = col[1].find_all("span", {"class": "star fill"})[-1].text
            if col[0].text == 'Food & Beverages':
                Food_Beverages = col[1].find_all("span", {"class": "star fill"})[-1].text
            if col[0].text == 'Inflight Entertainment':
                Inflight_Entertainment = col[1].find_all("span", {"class": "star fill"})[-1].text
            if col[0].text == 'Ground Service':
                Ground_Service = col[1].find_all("span", {"class": "star fill"})[-1].text
            if col[0].text == 'Wifi & Connectivity':
                Wifi_Connectivity = col[1].find_all("span", {"class": "star fill"})[-1].text
            if col[0].text == 'Value For Money':
                Value_For_Money = col[1].find_all("span", {"class": "star fill"})[-1].text
            if col[0].text == 'Recommended':
                Recommendend=col[1].text

        airline_data = airline_data.append({"ReviewBody":ReviewBody,
        "Aircraft":Aircraft,
        "Type Of Traveller":Type_Of_Traveller,
        "Seat Type":Seat_Type,
        "Route":Route,
        "Date Flown":Date_Flown,
        "Seat Comfort":Seat_comfort,
        "Cabin Staff Service":Cabin_Staff_service,
        "Food & Beverages":Food_Beverages,
        "Inflight Entertainment":Inflight_Entertainment,
        "Ground Service":Ground_Service,
        "Wifi & Connectivity":Wifi_Connectivity,
        "Value For Money":Value_For_Money,
        "Rating":Rating,
        "Recommendend":Recommendend}, ignore_index=True)

airline_data.to_csv("BA_reviews.csv")
    