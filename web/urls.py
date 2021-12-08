"""
Blueprint registration for full 'web' module
"""
from flask import Blueprint
from flask_lazyviews import LazyViews

from web.apps.auth.urls import AUTH_URLS
from web.apps.common.urls import COMMON_URLS

WEB_BLUEPRINT = Blueprint(
    'web', __name__,
    static_folder='static', static_url_path='/static/web',
    template_folder='templates'
)
VIEWS = LazyViews(WEB_BLUEPRINT)

# Add new urls
URLS = []
URLS.extend(AUTH_URLS)
URLS.extend(COMMON_URLS)

# load views
for url_name, view_name in URLS:
    VIEWS.add(url_name, view_name)
