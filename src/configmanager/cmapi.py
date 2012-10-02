"""
Save item value to memcache to improve performance.
"""
import jsonpickle
from google.appengine.api import memcache
from .models import ConfigItem

def getRawItems():
    items = []
    for item in ConfigItem.all():
        items.append({'key': item.key().name(), 'value': item.value,})
    return items

def _getCacheKey(key):
    return 'configitem-%s' % key

def _setCache(cachekey, jsonvalue):
    client = memcache.Client()
    oldvalue = client.gets(cachekey)
    success = False
    if not oldvalue:
        memcache.add(cachekey, jsonvalue)
        success = True
    else:
        if client.cas(cachekey, jsonvalue):
            success = True
    return success

def getItemValue(key):
    cachekey = _getCacheKey(key)
    jsonvalue = memcache.get(cachekey)
    if not jsonvalue:
        configitem = ConfigItem.get_by_key_name(key)
        if configitem:
            jsonvalue = jsonpickle.decode(configitem.value)
            _setCache(cachekey, jsonvalue)
    return jsonvalue

def saveItem(key, jsonvalue):
    strvalue = jsonpickle.encode(jsonvalue)
    item = ConfigItem(key_name=key, value=strvalue)
    item.put()
    cachekey = _getCacheKey(key)
    return _setCache(cachekey, jsonvalue)

