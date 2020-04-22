import configparser

meta = configparser.ConfigParser(interpolation=configparser.ExtendedInterpolation())

meta.read('meta.cfg')
app_name = meta['app']['name']

import os
import logging
from config import config
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

config_name = os.environ.get("{}_env".format(app_name), 'base')
current_config = config[config_name]

db = SQLAlchemy()
ma = Marshmallow()


def create_app(main=True):
    app = Flask(__name__)

    app.config.from_object(current_config)

    # Setup Flask-SQLAlchemy
    db.init_app(app)

    # Setup Flask-Marshmallow
    ma.init_app(app)

    # Register web application routes
    from .app import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # Register API routes
    from .api.v1.urls import api_v1 as api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api/v1')

    # TODO
    # Register Insert and Read routes

    log_file_handler = logging.FileHandler(current_config.LOG_FILE_LOCATION)
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(module)s -  %(message)s")

    log_file_handler.setLevel(current_config.LOG_LEVEL)
    log_file_handler.setFormatter(formatter)

    # remove existing handlers from Flask.logger
    app.logger.handlers.clear()

    # add new handlers to Flask.logger
    app.logger.addHandler(log_file_handler)
    app.logger.setLevel(current_config.LOG_LEVEL)

    app.logger.info("Server environment : {}".format(config_name))

    return app
