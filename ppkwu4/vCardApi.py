from flask import Flask

app = Flask(__name__)


@app.route('/')
def vCardApi():
    return 'Hello, World!'

app.run()