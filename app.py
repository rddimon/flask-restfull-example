"""
App creation
"""
from flask import Flask, session, g
from flasgger import Swagger

from database import users as db_users
from settings import current_config
from settings.basic_auth import BASIC_AUTH
from settings.jwt_auth import JWT
from api.urls import API_BLUEPRINT
from web.urls import WEB_BLUEPRINT


def create_app(config=None):
    """
    :param config:
    :return:
    """
    app = Flask(__name__)
    app.config.from_object(config)

    # blueprints registration
    app.register_blueprint(API_BLUEPRINT)
    app.register_blueprint(WEB_BLUEPRINT)

    # jwt initialization
    JWT.init_app(app)

    # basic auth initialization
    BASIC_AUTH.init_app(app)

    Swagger(app)

    @app.before_request
    def load_logged_in_user():
        """
        Get user by user id from session and load to app context.
        """
        user_id = session.get('user_id')

        if user_id is None:
            g.user = None
        else:
            g.user = db_users.get_user_by_id(user_id)[0]

    return app


APP = create_app(current_config)
