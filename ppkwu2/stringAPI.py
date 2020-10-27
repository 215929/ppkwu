from flask import Flask

app = Flask(__name__)


def check_for_lowercase(string_to_check):
    for char in string_to_check:
        if char.islower():
            return True
    return False


@app.route('/<string_to_check>')
def hello_world(string_to_check):
    if check_for_lowercase(string_to_check):
        return "true"
    return "false"


app.run()