# -*- coding: utf-8 -*-
import copy
import datetime

import unittest
import jsonpickle
import datetime
from pytz.gae import pytz

class TestJsonPickle(unittest.TestCase):

    def setUp(self):
        pass

    def testReference(self):
        n = datetime.datetime.utcnow()
        ns = [n, n]
        value = jsonpickle.encode(ns)
        print value # [{"py/repr": "datetime/datetime.datetime(2012, 10, 3, 12, 2, 13, 807462)"}, {"py/id": 0}]
        self.assertRaises(IndexError, jsonpickle.decode, value)

        ns = [n, copy.deepcopy(n)]
        value = jsonpickle.encode(ns)
        ns2 = jsonpickle.decode(value)
        self.assertEquals(ns, ns2)

    def testTimezone(self):
        nnow = datetime.datetime.now(tz=pytz.utc)
        strvalue = jsonpickle.encode(nnow)
        print 'date', strvalue
        value = jsonpickle.decode(strvalue)
        self.assertIsNone(value)

    def testLxml(self):
        # lxml.etree._ElementUnicodeResult
        # jsonpickle.encode(_ElementUnicodeResult) will always return null
        # but json.dumps works fine
        # lxml.etree._ElementUnicodeResult.strip() return basestring
        pass

if __name__ == '__main__':
    unittest.main()

