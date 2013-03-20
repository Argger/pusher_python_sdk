#!/usr/bin/python
from RequestCore import *
import urllib
#url = 'http://localhost:1234/rest/2.0/channel/channel'
url = 'http://10.23.248.79:8050/rest/2.0/channel/channel'
#url = 'http://www.baidu.com'
#body = 'start=0&limit=20&tag=abcd&method=fetch_tag&timestamp=1363697692&apikey=GkWwrvZrCaMQfCZ190ujndZm&sign=9fa0fa7baf1d43c17d38ee2841743083'
body = {'method':'fetch_tag', 'apikey':'GkWwrvZrCaMQfCZ190ujndZm'}

headers = dict()
headers['Content-Type'] = 'application/x-www-form-urlencoded'
headers['User-Agent'] = 'Baidu Channel Service Phpsdk Client'
request = RequestCore(url)
request.add_header('Content-Type', headers['Content-Type'])
request.add_header('User-Agent', headers['User-Agent'])
request.set_body(urllib.urlencode(body))

#print 'xxxxxxxxxxxxxx: ',request.request_headers
request.handle_request()
print 'xxxxxxxxxxxxxxxxxxxxxxxxx'
print request.response_headers
print request.response_body
print request.response_code

