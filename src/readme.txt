All the modules should contain version info and official download info

# lxml
lxml on google app engine: If you use python2.7 on AppEngine, the lxml library is supported.
local test: sudo apt-get install python-lxml
python-lxml_2.3-0.1build1_amd64.deb

# cssselect and pyquery
cssselect 0.7.1: http://pypi.python.org/pypi/cssselect
pyquery 1.2.1: http://pypi.python.org/pypi/pyquery

# httplib2 and oauth2
httplib2: http://httplib2.googlecode.com/files/httplib2-0.7.6.zip
https://github.com/simplegeo/python-oauth2

simplegeo/python-oauth2 to_url encoding bug:
https://github.com/simplegeo/python-oauth2/pull/91    Fix UnicodeEncodeError in urllib if non-ascii characters are present in Request parameters

# jsonpickle
http://pypi.python.org/packages/source/j/jsonpickle/jsonpickle-0.4.0.tar.gz
lxml.etree._ElementUnicodeResult can not be encoded by jsonpickle; jsonpickle.encode(lxml.etree._ElementUnicodeResult) always return null
jsonpickle does not support timezone

# yaml module 
It is default module on GAE.
But It can not be loaded by export PYTHONPATH="$HOME/bin/google_appengine:$PYTHONPATH"
Then we can not run unit test which depends on google.appengine.ext.db
Manually install in on local: download from "http://pyyaml.org/wiki/PyYAML", run "sudo python setup.py install"

# gaepytz
gaepytz-2011h
http://pypi.python.org/pypi/gaepytz

Asia/Shanghai: +08:06
Available timezone can be seen in __init__.py

# smallseg
smallseg_0.6.tar.gz
https://code.google.com/p/smallseg/

# jieba
jieba-0.25.zip
https://pypi.python.org/pypi/jieba/
I do some changes to jieba/__init__.py:
1. add initialize method to do initilize explicitly;
2. jieba.cache,jieba.small.cache files can be used to avoid file write operation and then can works on GAE.

# yuicompressor
http://yui.github.com/yuicompressor/
http://yuilibrary.com/download/builder/
YUI Build Tool(builder\componentbuild\lib\yuicompressor\yuicompressor-2.4.2.jar)

# jQCloud
https://github.com/lucaong/jQCloud

# jquery base64
https://github.com/yckart/jquery.base64.js

# jquery-cookie
https://github.com/carhartl/jquery-cookie

