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

    """
    clean_html will generate a copy of the old one, the the new copy celement.parent is None
    """
    def testCleanParent(self):
        content = """<html><body><DIV class="c1" title="title1"><a>link<span>1</span><script>2</script></a></DIV><script>s</script></body></html>"""
        htmlelement = lxml.html.fromstring(content)
        child = htmlelement.getchildren()[0].getchildren()[0]
        cleaner = lxml.html.clean.Cleaner()
        cchild = cleaner.clean_html(child)
        self.assertIsNotNone(child.getparent())
        self.assertIsNone(cchild.getparent())

    """One advantage of the lxml view is that a tree is now made of only one type of node: each node is an Element instance.
    .tail
    The text following the element. This is the most unusual departure. In the DOM model, any text following an element E is associated with the parent of E; in lxml, that text is considered the “tail” of E.

    lxml.HTMLElement.text and lxml.HTMLElement.tail    
    These are where lxml put text node.    
    There are no text node in lxml.
    Text node is field of HTMLElement, not children.
    """
    def testTextNode(self):
        content = """
        <body>123<div>abc.<br>efg.<br>hij</div>456</body>
        """
        htmlelement = lxml.html.fromstring(content)
        # element.tail is not part of element.text_content()
        # div.tail is 456, which is the text node after div.
        print 'htmlelement.tail'
        count = 0
        for child in htmlelement.iter():
            count += 1
            print child, child.text, 'end', child.tail
        self.assertEquals(count, 4)
        print 'htmlelement.itertext'
        count = 0
        for child in htmlelement.itertext():
            count += 1
        self.assertEquals(count, 5)

    """
    ValueError: Unicode strings with encoding declaration are not supported.
    """
    def testUnicodeEncoding(self):
        content = u'<?xml version="1.0" encoding="utf-8" ?><foo><bar/></foo>'
        self.assertRaises(ValueError, lxml.html.fromstring, content)

    """
    A fix has been submitted for lxml 2.3.1:
    https://github.com/lxml/lxml/commit/c531d3326cd1e6fd888299518d49acad5fd3b627
    """
    def testCleanerBug(self):
        content = '<ZyNETERROR>Parsing form data failed.</ZyNETERROR>'
        element = lxml.html.fromstring(content)
        cleaner = lxml.html.clean.Cleaner()
        # assert parent is not None
        self.assertRaises(AssertionError, cleaner.clean_html, element)

if __name__ == '__main__':
    unittest.main()

