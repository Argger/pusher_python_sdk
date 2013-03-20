#!/usr/bin/python

import pycurl
import StringIO
url='www.baidu.com'
c=pycurl.Curl()
c.setopt(c.URL, url)
b = StringIO.StringIO()   
c.setopt(c.WRITEFUNCTION, b.write)
c.setopt(c.FOLLOWLOCATION, 1)
c.setopt(c.HEADER, True)
c.perform()   
html=b.getvalue()   
print html
b.close()
c.close()
