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

    def testCleaner(self):
        content = u"""<a href="/page.do?pa=402880202405002801240882b84702d7&amp;guid=3f7e8eabae934b27a3b5320264a0db5b&amp;og=8a81f3f133d01e170133d36bed3c04d3" target="_blank"><font color="#A40106"><script>

				var a="民生为本 人才优先&lt;br&gt;";
				document.write(a);
				</script>民生为本 人才优先<br></font></a>"""
        htmlelement = lxml.html.fromstring(content)
        cleaner = lxml.html.clean.Cleaner()
        cleanedelement = cleaner.clean_html(htmlelement)# clean 'a' element
        self.assertTrue(type(cleanedelement) == lxml.html.HtmlElement)
        cleanedtext = cleanedelement.text_content()
        print cleanedtext
        self.assertEquals(cleanedtext, u'民生为本 人才优先')


if __name__ == '__main__':
    unittest.main()

