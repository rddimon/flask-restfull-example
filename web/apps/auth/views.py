"""
Common web app endpoints handling
"""
from flask import flash, redirect, render_template, request, session, url_for
from flask.views import MethodView
from flask_bcrypt import Bcrypt

from database import users as users_db

BCRYPT = Bcrypt()
REDIRECT_URL = 'common.index'
LOGIN_TEMPLATE = 'auth/login.html'


class WebLoginView(MethodView):
    """
    Login class.
    """

    def get(self):
        """
        Render login html template.
        """
        return render_template(LOGIN_TEMPLATE)

    def post(self):
        """
        Basic session auth. Check username and password hash. Add user id to session.
        """
        username = request.form['username']
        password = request.form['password']
        error = None
        user = users_db.get_user_by_username(username)

        if not user:
            error = 'Incorrect username.'
        elif not BCRYPT.check_password_hash(user[0]['password'], password):
            error = 'Incorrect password.'

        flash(error)

        if error is None:
            session.clear()
            session['user_id'] = str(user[0]['_id'])

        return redirect(url_for(REDIRECT_URL))


class WebLogoutView(MethodView):
    """
    Logout class.
    """

    def get(self):
        """
        Clear session storage. Redirect to home.
        """
        session.clear()
        return redirect(url_for(REDIRECT_URL))
