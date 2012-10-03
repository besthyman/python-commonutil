# -*- coding: utf-8 -*-
import copy
import datetime

import unittest
import jsonpickle

class TestJsonPickle(unittest.TestCase):

    def setUp(self):
        pass

    def testBasic(self):
        n = datetime.datetime.utcnow()
        ns = [n, n]
        value = jsonpickle.encode(ns)
        print value # [{"py/repr": "datetime/datetime.datetime(2012, 10, 3, 12, 2, 13, 807462)"}, {"py/id": 0}]
        self.assertRaises(IndexError, jsonpickle.decode, value)

        ns = [n, copy.deepcopy(n)]
        value = jsonpickle.encode(ns)
        ns2 = jsonpickle.decode(value)
        self.assertEquals(ns, ns2)


if __name__ == '__main__':
    unittest.main()

