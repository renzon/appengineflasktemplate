from flask import Blueprint

app = Blueprint('subscription', __name__)


@app.route('')
def form():
    return 'foo'
