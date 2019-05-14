"""
Common web app urls
"""

from . import views

COMMON_URLS = [
    ('/', views.RenderTemplateView.as_view('index', template_name='common/index.html')),
]
