#!/usr/bin/python


import pycurl
import StringIO
import urllib
 
url = "http://10.23.248.79:8050/rest/2.0/channel/channel"
post_data_dic = {'method':'fetch_tag', 'apikey':'GkWwrvZrCaMQfCZ190ujndZm'}
crl = pycurl.Curl()
crl.setopt(pycurl.VERBOSE,1)
crl.setopt(pycurl.FOLLOWLOCATION, 1)
crl.setopt(pycurl.MAXREDIRS, 5)
#crl.setopt(pycurl.AUTOREFERER,1)
 
crl.setopt(pycurl.CONNECTTIMEOUT, 60)
crl.setopt(pycurl.TIMEOUT, 300)
#crl.setopt(pycurl.PROXY,proxy)
crl.setopt(pycurl.HTTPPROXYTUNNEL,1)
#crl.setopt(pycurl.NOSIGNAL, 1)
crl.fp = StringIO.StringIO()
header = StringIO.StringIO()
crl.setopt(pycurl.USERAGENT, "dhgu hoho")
 
# Option -d/--data <data>   HTTP POST data
crl.setopt(crl.POSTFIELDS,  urllib.urlencode(post_data_dic))
 
crl.setopt(pycurl.URL, url)
crl.setopt(crl.HEADERFUNCTION, header.write)
crl.setopt(crl.WRITEFUNCTION, crl.fp.write)
crl.perform()

#print crl.body()


code = crl.getinfo(pycurl.HTTP_CODE)
#header = crl.getinfo(pycurl.HEADER)
header_size = crl.getinfo(pycurl.HEADER_SIZE)
#content_type = crl.getinfo(pycurl.CONTENT_TYPE) 
print "head:>>",header.getvalue()
print len(header.getvalue())
print crl.fp.getvalue()
print code
print header_size
#print content_type
