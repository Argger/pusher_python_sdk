#!/usr/bin/python
# _*_ coding: UTF-8 _*_

import sys
import time
sys.path.append("..")
from Channel import *

#以下只是测试数据，请使用者自行修改为可用数据
apiKey = "76Yi0ZBGGV2HrAziIiYEFtRh"
secretKey = "xxxxxxxxxxxxx"
user_id = "1105115563847474869"
channel_id = 3944730196422489622

message = "{'title':'baidu push','description':'message from python sdk'}"
#message = json.dumps(message)
message_key = "key1"
#message_key = json.dumps(message_key)
tagname = "test_tag"

def test_pushMessage_to_user():
	c = Channel(apiKey, secretKey)
	push_type = 1
	optional = dict()
	optional[Channel.USER_ID] = user_id
	optional[Channel.CHANNEL_ID] = channel_id
	#推送通知类型
	optional[Channel.MESSAGE_TYPE] = 1
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

def test_verifyBind():
	c = Channel(apiKey, secretKey)
	optional = dict()
	optional[Channel.DEVICE_TYPE] = 3;
	ret = c.verifyBind(user_id, optional)
	print ret

def test_fetchMessage():
	c = Channel(apiKey, secretKey)
	ret = c.fetchMessage(user_id)
	print ret	

def test_deleteMessage():
	c = Channel(apiKey, secretKey)
	msg_id = "111"
	ret = c.deleteMessage(user_id, msg_id)
	print ret

def test_setTag():
	c = Channel(apiKey, secretKey)
	optional = dict()
	optional[Channel.USER_ID] = user_id
	ret = c.setTag(tagname, optional)
	print ret

def test_fetchTag():
	c = Channel(apiKey, secretKey)
	ret = c.fetchTag()
	print ret

def test_deleteTag():
	c = Channel(apiKey, secretKey)
	optional = dict()
	optional[Channel.USER_ID] = user_id
	ret = c.deleteTag(tagname, optional)
	print ret

def test_queryUserTag():
	c = Channel(apiKey, secretKey)
	ret = c.queryUserTag(user_id)
	print ret

def test_queryDeviceType():
	c = Channel(apiKey, secretKey)
	ret = c.queryDeviceType(channel_id)
	print ret

test_pushMessage_to_user()
"""
if(__name__ == '__main__'):
	test_pushMessage_to_user()
	time.sleep(1)
	test_pushMessage_to_tag()
	time.sleep(1)
	test_pushMessage_to_all()
	time.sleep(1)
	test_queryBindList()
	time.sleep(1)
	test_verifyBind()
	time.sleep(1)
	test_fetchMessage()	
	time.sleep(1)
	test_deleteMessage()
	time.sleep(1)
	test_setTag()
	time.sleep(1)
	test_fetchTag()
	time.sleep(1)
	test_deleteTag()
	time.sleep(1)
	test_queryUserTag()
	time.sleep(1)
	test_queryDeviceType()
	time.sleep(1)
"""
