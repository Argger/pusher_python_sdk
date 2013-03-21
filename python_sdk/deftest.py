#!/usr/bin/python

from Channel import *

accessKey = 'GkWwrvZrCaMQfCZ190ujndZm'
secretKey = 'I5nqT2szvC12Qdf1gHZ5RSpPnluVo4VI'

user_id = '580118370301074982'
channel_id = '3915728604212165383'
message = 'helloworld'
message_key = 'key'

c = Channel('00', '11')
c.setApiKey(accessKey)
c.setSecretKey(secretKey)
print c._apiKey
print c._secretKey
print c._curlOpts

optional = dict()
optional[Channel.DEVICE_TYPE] = 3
ret = c.queryBindList(user_id, optional)

push_type = 1
optional = dict()
optional[Channel.USER_ID] = user_id
#ret = c.pushMessage(push_type, message, message_key, optional)
print ret
