from flask import Flask
from flask_cors import CORS
#from services.blueprint import api
from services.blueprint.web import blueprint
from services.settings import DevConfig


def home(config_object=DevConfig):
    app = Flask(__name__)
    app.config.from_object(config_object)

    #app.register_blueprint(api.blueprint)
    app.register_blueprint(blueprint)

    CORS(app)

    return app

