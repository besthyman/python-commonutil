# -*- coding: utf-8 -*-

import unittest

import datetime
from pytz.gae import pytz

class TestBase(unittest.TestCase):

    def setUp(self):
        pass

    def testBasic(self):
        date_format = '%m/%d/%Y %H:%M:%S %Z'
        date = datetime.datetime.now(tz=pytz.utc)
        print 'Current date & time is:', date.strftime(date_format)

        # must run on GAE environment?
        date = date.astimezone(pytz.timezone('US/Pacific'))

        print 'Local date & time is  :', date.strftime(date_format)
        self.assertIsNotNone(date)

if __name__ == '__main__':
    unittest.main()

