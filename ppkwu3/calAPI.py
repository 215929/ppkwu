from flask import Flask
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)


@app.route('/')
def hello():
    response = requests.get(
        "http://www.weeia.p.lodz.pl/pliki_strony_kontroler/kalendarz.php?rok=2020&miesiac=10&lang=1")
    return_value = ""

    parsed_html = BeautifulSoup(response.text)
    return_value = parsed_html.find_all('a')

    return str(return_value)
    # return "Hello"


app.run()
