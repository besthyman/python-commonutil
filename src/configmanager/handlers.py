import logging
import os

from google.appengine.ext.webapp import template
import webapp2

import jsonpickle

from . import cmapi

class MainPage(webapp2.RequestHandler):

    def _render(self, templateValues):
        self.response.headers['Content-Type'] = 'text/html'
        path = os.path.join(os.path.dirname(__file__), 'templates', 'index.html')
        self.response.out.write(template.render(path, templateValues))

    def get(self, message=''):
        items = cmapi.getRawItems()
        key = self.request.get('key')
        value = self.request.get('value')
        keys = []
        for item in items:
            keys.append(item['key'])
            if key and not value and item['key'] == key:
                value = item['value']
        keys.sort()
        templateValues = {
            'key': key,
            'value': value,
            'keys': keys,
            'items': items,
            'message': message,
        }
        self._render(templateValues)

    def post(self):
        key = self.request.get('key')
        value = self.request.get('value')
        message = ''
        try:
            if value:
                jsonvalue = jsonpickle.decode(value)
                if not cmapi.saveItem(key, jsonvalue):
                    message = 'Failed to put value into cache and db.'
            else:
                if not cmapi.removeItem(key):
                    message = 'Failed to delete value from cache and db.'
        except ValueError:
            message = 'Failed to decode the input value.'
        self.get(message=message)

