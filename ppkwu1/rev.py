from flask import Flask

app = Flask(__name__)


@app.route('/ppkw/rev/<word_to_reverse>')
def hello(word_to_reverse):
    return word_to_reverse[::-1]


app.run()
