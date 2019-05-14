"""
Common web app urls
"""

from . import views

AUTH_URLS = [
    ('/login', views.WebLoginView.as_view('login')),
    ('/logout', views.WebLogoutView.as_view('logout'))
]
