from flask import Flask
from  flask_sqlalchemy import SQLAlchemy
from config import config
import os

app = Flask(__name__)

db = SQLAlchemy()

config_name=os.getenv('FLASK_CONFIG') or 'default'

def create_app():
    db.__init__(app)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    from .api import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/api')
    return app

