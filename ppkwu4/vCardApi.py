from flask import Flask, Response
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)


@app.route('/')
def vCardApi():
    response = requests.get(
        "https://panoramafirm.pl/szukaj?k=Hydraulik&l=")

    parsed_html = BeautifulSoup(response.text)
    return_value1 = []

    for link in parsed_html.find_all('a', {"title": "Zobacz informacje szczegółowe o firmie"}):
        return_value1.append(link.getText)

    return_value2 = []

    for div in parsed_html.find_all('div', {"class": "address"}):
        return_value2.append(div.getText)

    return_value3 = []

    for link in parsed_html.find_all('a', {"class": "icon-telephone"}):
        return_value3.append(link['title'])

    return_value4 = []

    for link in parsed_html.find_all('a', {"class": "ajax-modal-link"}):
        return_value4.append(link['data-company-email'])

    return str([return_value1, return_value2, return_value3, return_value4])


app.run()