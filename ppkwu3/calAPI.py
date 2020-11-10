from flask import Flask
import requests

app = Flask(__name__)


@app.route('/')
def hello():
    response = requests.get("http://www.weeia.p.lodz.pl/pliki_strony_kontroler/kalendarz.php?rok=2020&miesiac=10&lang=1")
    return response.text
    #return "Hello"


app.run()
