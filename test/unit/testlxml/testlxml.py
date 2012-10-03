# -*- coding: utf-8 -*-

import unittest
import lxml.html
import lxml.html.clean

class TestLxml(unittest.TestCase):

    def setUp(self):
        pass

    def testBasic(self):
        content = """<html><body><DIV class="c1" title="title1"><a>link<span>1</span><script>2</script></a></DIV><script>s</script></body></html>"""
        htmlelement = lxml.html.fromstring(content)
        self.assertTrue(type(htmlelement) == lxml.html.HtmlElement)
        self.assertEquals(htmlelement.text_content(), 'link12s')

        # lxml.text_content() will return script tag content
        cleaner = lxml.html.clean.Cleaner()
        cleanedelement = cleaner.clean_html(htmlelement[0][0][0])# clean 'a' element
        self.assertTrue(type(cleanedelement) == lxml.html.HtmlElement)
        self.assertEquals(cleanedelement.tag, 'a')
        self.assertEquals(cleanedelement.text_content(), 'link1')

        # clean operation creates a new element, and does not affect the original one.
        self.assertEquals(htmlelement.text_content(), 'link12s')


if __name__ == '__main__':
    unittest.main()

