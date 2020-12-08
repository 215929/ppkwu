from flask import Flask, Response
import requests
from bs4 import BeautifulSoup
import vobject

app = Flask(__name__)


@app.route('/')
def vCardApi():
    response = requests.get(
        "https://panoramafirm.pl/szukaj?k=Hydraulik&l=")

    parsed_html = BeautifulSoup(response.text)

    users = []

    names = []
    for link in parsed_html.find_all('a', {"class": "company-name"}):
        names.append(link.text.strip())

    addresses = []
    for div in parsed_html.find_all('div', {"class": "address"}):
        addresses.append(div.text.strip())

    phones = []
    for link in parsed_html.find_all('a', {"class": "icon-telephone"}):
        phones.append(link['title'])

    mails = []
    for link in parsed_html.find_all('a', {"class": "ajax-modal-link"}):
        mails.append(link['data-company-email'])

    for i in range(len(names)):
        users.append({
            "name": names[i],
            "address": addresses[i],
            "phone": phones[i],
            "mail": mails[i],
        })

    vCards = []
    for user in users:
        v = vobject.vCard()
        v.add('fn').value = user["name"]
        v.add('address').value = user["address"]
        v.add('tel').value = user["phone"]
        v.add('email').value = user["mail"]
        v = v.serialize()
        print(v)
        vCards.append(v)

    return str(vCards)


app.run()
