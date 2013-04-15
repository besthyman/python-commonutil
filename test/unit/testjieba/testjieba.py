# -*- coding: utf-8 -*-
import copy
import datetime

import unittest
import jsonpickle
import datetime
from pytz.gae import pytz

class TestJieba(unittest.TestCase):

    def setUp(self):
        pass

    def testReference(self):
        import jieba # May fail to load jieba
        jieba.initialize(usingSmall=False)
        import jieba.posseg as pseg
        pwords = []
        content = u'上海今日新确诊3例人感染H7N9禽流感病例'
        _ = """
ns 上海
t 今日
a 新
v 确诊
m 3
n 例人
v 感染
eng H7N9
n 禽流感
n 病例
"""
        content = u'李克强：在半岛挑事无异于搬石头砸自己脚'
        _ = """
nr 李克强
p 在
n 半岛
v 挑事
l 无异于
v 搬
l 石头砸
r 自己
n 脚
"""
        for word in pseg.cut(content):
            print word.flag, word.word

if __name__ == '__main__':
    unittest.main()

