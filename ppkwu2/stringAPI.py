from flask import Flask

app = Flask(__name__)


@app.route('/<string_to_check>')
def hello_world(string_to_check):
    return string_to_check


app.run()