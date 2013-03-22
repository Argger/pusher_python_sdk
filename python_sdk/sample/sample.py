#!/usr/bin/python
import sys
sys.path.append("..")
from Channel import *

apiKey = 'GkWwrvZrCaMQfCZ190ujndZm'
secretKey = 'I5nqT2szvC12Qdf1gHZ5RSpPnluVo4VI'

user_id = '580118370301074982'
channel_id = '3915728604212165383'
message = ['helloworld', 'hellopush']
message = json.dumps(message)
message_key = ['key1', 'key2']
message_key = json.dumps(message_key)
#message = 'hello world'
#message_key = 'key'

def test_pushMessage_to_user():
	c = Channel(apiKey, secretKey)
	push_type = 1
	optional = dict()
	optional[Channel.USER_ID] = user_id
	ret = c.pushMessage(push_type, message, message_key, optional)
	print ret

def test_pushMessage_to_tag():
	c = Channel(apiKey, secretKey)
	push_type = 2
	tag_name = 'push'
	optional = dict()
	optional[Channel.TAG_NAME] = tag_name
	ret = c.pushMessage(push_type, message, message_key, optional)
	print ret

def test_pushMessage_to_all():
	c = Channel(apiKey, secretKey)
	push_type = 3
	optional = dict()
	ret = c.pushMessage(push_type, message, message_key, optional)
	print ret


def test_queryBindList():
	c = Channel(apiKey, secretKey)
	optional = dict()
	optional[Channel.CHANNEL_ID] =  channel_id
	ret = c.queryBindList(user_id, optional)	
	print ret


test_pushMessage_to_user()
test_pushMessage_to_tag()
#test_pushMessage_to_all()
test_queryBindList()

