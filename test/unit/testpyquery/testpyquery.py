# -*- coding: utf-8 -*-

import unittest
import lxml
import pyquery

class TestPyQuery(unittest.TestCase):

    def setUp(self):
        pass

    def testBasic(self):
        content = """<html><body>
<DIV class="c1" title="title1"><a>link<span>1</span></a></DIV>
<DIV class="c1" title="title1"><a>link<span>1</span></a></DIV>
</body></html>
"""
        htmlelement = lxml.html.fromstring(content)
        self.assertTrue(type(htmlelement) == lxml.html.HtmlElement)

        rootqueryobj = pyquery.PyQuery(htmlelement)
        self.assertTrue(type(rootqueryobj) == pyquery.pyquery.PyQuery)

        queryobj = rootqueryobj('div.cnot')
        self.assertEquals(len(queryobj), 0)

        queryobj = rootqueryobj('div.c1:first')
        self.assertTrue(type(queryobj) == pyquery.pyquery.PyQuery)
        self.assertEquals(len(queryobj), 1)

        htmlelement = queryobj[0]
        self.assertEquals(htmlelement.tag, 'div')
        self.assertEquals(htmlelement.text_content(), 'link1')
        self.assertEquals(htmlelement.get('title'), 'title1')
        self.assertIsNone(htmlelement.get('title2'))

if __name__ == '__main__':
    unittest.main()

