from google.appengine.ext import vendor

import subscription

vendor.add('lib')

from core.main import app

app.register_blueprint(subscription.blueprint, url_prefix='/inscricao')
