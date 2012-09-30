import os
import webapp2
from google.appengine.ext.webapp import template
from .models import ConfigItem

class MainPage(webapp2.RequestHandler):
    def _render(self, templateValues):
        self.response.headers['Content-Type'] = 'text/html'
        path = os.path.join(os.path.dirname(__file__), 'templates', 'index.html')
        self.response.out.write(template.render(path, templateValues))

    def get(self):
        items = []
        for item in ConfigItem.all():
            items.append({'key': item.key().name(), 'value': item.value,})
        templateValues = {
            'items': items,
        }
        self._render(templateValues)

    def post(self):
        key = self.request.get('key')
        value = self.request.get('value')
        if key:
            item = ConfigItem(key_name=key, value=value)
            item.put()
        self.get()

