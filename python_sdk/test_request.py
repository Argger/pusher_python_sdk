#!/usr/bin/python
from RequestCore import *

url = 'http://10.23.248.79:8050/rest/2.0/channel/channel'
body = 'start=0&limit=20&tag=abcd&method=fetch_tag&timestamp=1363697692&apikey=GkWwrvZrCaMQfCZ190ujndZm&sign=9fa0fa7baf1d43c17d38ee2841743083'
request = RequestCore(url)
request.set_method('POST')
request.set_body(body)

request.send_request()
