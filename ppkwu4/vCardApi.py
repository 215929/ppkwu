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
    rowHTML += "<td>  <a href=\"/downloadVCard/name=" + user["name"]\
               + "&&address=" + user["address"]\
               + "&&phone=" + user["phone"]\
               + "&&mail=" + user["mail"]\
               + "\">wygeneruj vCard</td>\n"

    rowHTML += "</tr>\n"

    return rowHTML


@app.route('/vCardApi/profession=<profession>')
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

    return generateTable(users)


@app.route('/downloadVCard/name=<name>&&address=<address>&&phone=<phone>&&mail=<mail>')
def downloadVCard(name, address, phone, mail):
    v = vobject.vCard()
    v.add('fn').value = name if name else "brak"
    v.add('address').value = address if address else "brak"
    v.add('tel').value = phone if phone else "brak"
    v.add('email').value = mail if mail else "brak"
    v = v.serialize()

    return Response(v, mimetype="text/vcf",
                    headers={"Content-Disposition": "attachment;filename=vcard.vcf"})

app.run()
