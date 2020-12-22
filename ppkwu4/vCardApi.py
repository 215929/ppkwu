from flask import Flask, Response
import requests
from bs4 import BeautifulSoup
import vobject

app = Flask(__name__)


def generateTable(users):
    tableHTML = "<table style=\"width:100%\">\n"

    for user in users:
        tableHTML += generateRow(user)

    tableHTML += "</table>\n"

    return tableHTML


def generateRow(user):
    rowHTML = "<tr>\n"

    rowHTML += "<td>" + user["name"] + "</td>\n"
    rowHTML += "<td>" + user["address"] + "</td>\n"
    rowHTML += "<td>" + user["phone"] + "</td>\n"
    rowHTML += "<td>" + user["mail"] + "</td>\n"
    rowHTML += "<td>  <a href=\"https://www.w3schools.com\">Visit W3Schools</a>  </td>\n"

    rowHTML += "</tr>\n"

    return rowHTML


def generateVCard(user):
    v = vobject.vCard()
    v.add('fn').value = user["name"]
    v.add('address').value = user["address"]
    v.add('tel').value = user["phone"]
    v.add('email').value = user["mail"]
    v = v.serialize()
    return v


@app.route('/profession=<profession>')
def vCardApi(profession):
    response = requests.get(
        "https://panoramafirm.pl/szukaj?k=" + str(profession) + "&l=")

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
        vCards.append(generateVCard(user))

    return generateTable(users)


app.run()
