#!/usr/bin/python

from Channel import *

apiKey = 'GkWwrvZrCaMQfCZ190ujndZm'
secretKey = 'I5nqT2szvC12Qdf1gHZ5RSpPnluVo4VI'

user_id = '580118370301074982'
channel_id = '3915728604212165383'
message = ['helloworld', 'hellopush']
message_key = ['key1', 'key2']
#message = 'hello world'
#message_key = 'key'
c = Channel(apiKey, secretKey)
#ret = c.queryBindList(user_id)

push_type = 1
optional = dict()
#optional[Channel.USER_ID] = user_id
#optional[Channel.TAG_NAME] = 'push'
ret = c.pushMessage(message, message_key, optional)
print ret
