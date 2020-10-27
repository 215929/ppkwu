from flask import Flask

app = Flask(__name__)


def check_for_lowercase(string_to_check):
    for char in string_to_check:
        if char.islower():
            return True
    return False


def check_for_uppercase(string_to_check):
    for char in string_to_check:
        if char.isupper():
            return True
    return False


def check_for_numbers(string_to_check):
    for char in string_to_check:
        if char.isnumeric():
            return True
    return False


def check_for_special_characters(string_to_check):
    for char in string_to_check:
        if not char.isalnum():
            return True
    return False


@app.route('/<string_to_check>')
def hello_world(string_to_check):
    return {
        "lowercase": check_for_lowercase(string_to_check),
        "uppercase": check_for_uppercase(string_to_check),
        "numbers": check_for_numbers(string_to_check),
        "special characters": check_for_special_characters(string_to_check)
    }


app.run()
