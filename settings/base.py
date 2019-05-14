"""
Base configuration setup
"""
import os
import datetime

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEFAULT_SECRET_KEY = 'Pikachu'


class Config(object):
    """
    Base configuration
    """
    DEBUG = False

    BASE_DIR = BASE_DIR

    SECRET_KEY = os.environ.get('SECRET_KEY', DEFAULT_SECRET_KEY)

    JWT_SECRET_KEY = os.environ.get('SECRET_KEY', DEFAULT_SECRET_KEY)
    JWT_ACCESS_TOKEN_EXPIRES = datetime.timedelta(minutes=5)
    JWT_BLACKLIST_ENABLED = True
    JWT_BLACKLIST_TOKEN_CHECKS = ['access', 'refresh']

    MONGO_DATABASES = {
        "app": {
            "username": os.environ.get('MONGO_USER'),
            "password": os.environ.get('MONGO_PASSWORD'),
            "port": 27017,
            "host": 'mongodb+srv://{}:{}@{}/'.format(
                os.environ.get('MONGO_USER'),
                os.environ.get('MONGO_PASSWORD'),
                os.environ.get('MONGO_HOST'),
            ),
        }
    }

    """
    PYLINT SETTINGS.
    Include files to be checked with full path as <file.py>
    Include modules to be checked with full path as <module/.>
    """
    PYLINT_SETTINGS = {
        "include": ['api/.', 'database/.', 'settings/.', 'web/.', 'app.py'],
        "report_directory_name": "data",
        "report_file_name": "report.txt",
        "config_directory_name": "settings",
        "config_file_name": ".pylintrc"
    }

    """
    Basic Auth Credentials
    """
    BASIC_AUTH_USERNAME = os.environ.get('BASIC_AUTH_USERNAME')
    BASIC_AUTH_PASSWORD = os.environ.get('BASIC_AUTH_PASSWORD')

    SWAGGER = {
        'title': 'flask restfull example',
        'version': 0.1
    }
