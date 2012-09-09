# -*- coding: utf-8 -*-

import datetime

def getIntByMinitue():
    date = datetime.datetime.utcnow()
    return (((date.year-1970) * 366 + date.month * 31) * 24 + date.hour) * 60 + date.minute

