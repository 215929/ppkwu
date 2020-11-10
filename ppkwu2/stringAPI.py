from flask import Flask

app = Flask(__name__)


def check_for_lowercase(string_to_check):
    if any(letter.islower() for letter in string_to_check):
        return True
    else:
        return False


def check_for_uppercase(string_to_check):
    if any(letter.isupper() for letter in string_to_check):
        return True
    else:
        return False


def check_for_numbers(string_to_check):
    if any(letter.isnumeric() for letter in string_to_check):
        return True
    else:
        return False


def check_for_special_characters(string_to_check):
    if any(not letter.isalnum() for letter in string_to_check):
        return True
    else:
        return False


@app.route('/stringAPI/<string_to_check>')
def hello_world(string_to_check):
    return {
        "lowercase": check_for_lowercase(string_to_check),
        "uppercase": check_for_uppercase(string_to_check),
        "numbers": check_for_numbers(string_to_check),
        "special characters": check_for_special_characters(string_to_check)
    }


app.run()
