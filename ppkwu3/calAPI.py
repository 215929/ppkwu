from flask import Flask
import requests
from bs4 import BeautifulSoup
from icalendar import Calendar, Event
import datetime

app = Flask(__name__)


@app.route('/')
def hello():
    response = requests.get(
        "http://www.weeia.p.lodz.pl/pliki_strony_kontroler/kalendarz.php?rok=2020&miesiac=10&lang=1")
    events = dict()
    event_list = []

    parsed_html = BeautifulSoup(response.text)

    event_list = parsed_html.find_all('div', {"class": "InnerBox"})

    for day in parsed_html.find_all('a', {"class": "active"}):
        events[day.getText()] = [day.get('href'), event_list.pop(0).text]

    cal = Calendar()

    return_value = []

    for day in events:
        #return_value.append(events[day][1])

        event = Event()

        event.add('summary', events[day][1])
        event.add('dtstart', datetime.date(2020, 10, int(day)))

        cal.add_component(event)

    f = open('test.ics', 'wb')
    f.write(cal.to_ical())
    f.close()

    return str(return_value)


app.run()
