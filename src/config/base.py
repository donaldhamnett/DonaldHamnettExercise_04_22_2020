import os
import logging
from app import app_name


class Config(object):

    DEBUG = True

    LOG_LEVEL = logging.DEBUG

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    LOG_FILE_LOCATION = f'{BASE_DIR}/log/{app_name}.log'

    SQLALCHEMY_DATABASE_URI = f'sqlite:///{BASE_DIR}/{app_name}.sqlite'
