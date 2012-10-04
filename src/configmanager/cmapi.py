"""
Save item value to memcache to improve performance.
"""
from google.appengine.api import memcache
from google.appengine.ext import db

import jsonpickle

from .models import ConfigItem

def getRawItems():
    items = []
    for item in ConfigItem.all():
        items.append({'key': item.key().name(), 'value': item.value,})
    return items

def _getCacheKey(key):
    return 'configitem-%s' % key

# thread safe visit to cache
def _setCache(cachekey, jsonvalue):
    client = memcache.Client()
    oldvalue = client.gets(cachekey)
    success = False
    if not oldvalue:
        memcache.set(cachekey, jsonvalue)
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
    cachekey = _getCacheKey(key)
    if not jsonvalue:
        return True
    success = _setCache(cachekey, jsonvalue)
    if success:# if we fail to save value to cache, we should not put it into db.
        strvalue = jsonpickle.encode(jsonvalue)
        item = ConfigItem(key_name=key, value=strvalue)
        item.put()
    return success

def removeItem(key):
    cachekey = _getCacheKey(key)
    memcache.delete(cachekey)
    keyobj = db.Key.from_path('ConfigItem', key)
    db.delete(keyobj)
    return True

