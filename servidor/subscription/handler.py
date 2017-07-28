from flask import Flask

app = Flask(__name__)


@app.route('/inscricao')
def form():
    return 'foo'
