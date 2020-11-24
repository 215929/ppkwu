from flask import Flask, send_file, Response
import requests
from bs4 import BeautifulSoup
from icalendar import Calendar, Event
import datetime

app = Flask(__name__)


@app.route('/calAPI/year=<year>/month=<month>')
def hello(month, year):
    response = requests.get(
        "http://www.weeia.p.lodz.pl/pliki_strony_kontroler/kalendarz.php?rok=" + year + "&miesiac=" + month + "&lang=1")
    events = dict()

    parsed_html = BeautifulSoup(response.text)

    event_list = parsed_html.find_all('div', {"class": "InnerBox"})

    for day in parsed_html.find_all('a', {"class": "active"}):
        events[day.getText()] = [day.get('href'), event_list.pop(0).text]

    cal = Calendar()

    for day in events:
        event = Event()

        event.add('summary', events[day][1])
        event.add('dtstart', datetime.date(int(year), int(month), int(day)))

        cal.add_component(event)

    return Response((cal.to_ical()), mimetype="text/ics",
                    headers={"Content-Disposition": "attachment;filename=test.ics"})


app.run()
