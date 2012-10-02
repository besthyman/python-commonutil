import jsonpickle
import os
import webapp2
from google.appengine.ext.webapp import template
from . import cmapi

class MainPage(webapp2.RequestHandler):

    def _render(self, templateValues):
        self.response.headers['Content-Type'] = 'text/html'
        path = os.path.join(os.path.dirname(__file__), 'templates', 'index.html')
        self.response.out.write(template.render(path, templateValues))

    def get(self):
        items = cmapi.getRawItems()
        templateValues = {
            'items': items,
        }
        self._render(templateValues)

    def post(self):
        key = self.request.get('key')
        value = self.request.get('value')
        jsonvalue = jsonpickle.decode(value)
        cmapi.saveItem(key, jsonvalue)
        self.get()

