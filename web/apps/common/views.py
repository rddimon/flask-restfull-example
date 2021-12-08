"""
Common web app endpoints handling
"""
from flask import render_template
from flask.views import View


class RenderTemplateView(View):
    def __init__(self, template_name):
        self.template_name = template_name

    def dispatch_request(self):
        return render_template(self.template_name)
