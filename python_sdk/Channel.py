#!/usr/bin/python
# _*_ coding: UTF-8 _*_
import time
import urllib
import md5
import json
import ChannelException
from RequestCore import *

#
#
#

#
# Channel
#

class Channel(object):
	TIMESTAMP = 'timestamp'
	EXPIRES = 'expires'
	VERSION = 'v'
	CHANNEL_ID = 'channel_id'
	USER_TYPE = 'user_type'
	DEVICE_TYPE = 'device_type'
	PAGENO = 'pageno'
	LIMIT = 'limit'
	
	MSG_IDS = 'msg_ids'
	MSG_KEYS = 'msg_keys'
	IOS_MESSAGES = 'ios_messages'
	WP_MESSAGES = 'wp_messages'
	
	MESSAGE_TYPE = 'message_type'
	MESSAGE_EXPIRES = 'message_expires'
	GROUP_NAME = 'name'
	GROUP_INFO = 'info'
	GROUP_ID = 'gid'
	BANNED_TIME = 'banned_time'
	CALLBACK_DOMAIN = 'domain'
	CALLBACK_URI = 'uri'
	
	APPID = 'appid'
	ACCESS_TOKEN = 'access_token'
	API_KEY = 'apikey'
	SECRET_KEY = 'secret_key'
	SIGN = 'sign'
	METHOD = 'method'
	HOST = 'host'
	USER_ID = 'user_id'
	MESSAGES = 'messages'
	PRODUCT = 'channel'
	
	DEFAULT_HOST = '10.23.248.79:8050' #'channel.api.duapp.com'
#	DEFAULT_HOST = 'localhost:1234' #'channel.api.duapp.com'
	NAME = 'name'
	DESCRIPTION = 'description'
	CERT = 'cert'
	RELEASE_CERT = 'release_cert'
	DEV_CERT = 'dev_cert'
	PUSH_TYPE = 'push_type'

	#推送类型常量
	PUSH_TO_USER = 1
	PUSH_TO_GROUP = 2
	PUSH_TO_ALL = 3
	PUSH_TO_DEVICE = 4

	#Channel 错误常量
	CHANNEL_SDK_SYS = 1
	CHANNEL_SDK_INIT_FAIL = 2
	CHANNEL_SDK_PARAM = 3
	CHANNEL_SDK_HTTP_STATUS_ERROR_AND_RESULT_ERROR = 4
	CHANNEL_SDK_HTTP_STATUS_OK_BUT_RESULT_ERROR = 5
	
	
	
	#Channel 私有变量
	#用户关注： 否
	
	def __init__(self, apiKey, secretKey, arr_curlOpts = None):
		self._apiKey = apiKey
		self._secretKey = secretKey
		self._requestId = 0
		if arr_curlOpts is None:
			self._curlOpts = dict(CURLOPT_TIMEOUT = 30, CURLOPT_CONNECTTIMEOUT = 5)
		else:
			self._curlOpts = arr_curlOpts

		self._arrayErrorMap = {'0' : 'python sdk error',\
									Channel.CHANNEL_SDK_SYS : 'php sdk error',\
									Channel.CHANNEL_SDK_INIT_FAIL : 'php sdk init error', \
									Channel.CHANNEL_SDK_PARAM : 'lack param', \
									Channel.CHANNEL_SDK_HTTP_STATUS_ERROR_AND_RESULT_ERROR : 'http status is error, and the body returned is not a json string', \
									Channel.CHANNEL_SDK_HTTP_STATUS_OK_BUT_RESULT_ERROR : 'http status is ok, but the body returned is not a json string'}
		
		if(not isinstance(self._curlOpts, dict)):
			raise ChannelExcepthion, ('invalid param -arr_curlopt is not an dict', Channel.CHANNEL_SDK_INIT_FAIL) 

		self._resetErrorStatus()

#################################################

	def queryBindList(self, userId, optional = None):
		self._resetErrorStatus()
		tmpArgs = [userId, optional]
		arrArgs = self._mergeArgs([Channel.USER_ID], tmpArgs)	
		arrArgs[Channel.METHOD] = 'query_bindlist'
		return self._commonProcess(arrArgs)
		
			





##################################################

	def _resetErrorStatus(self):
		pass

#########################################################	

	def _checkString(self, string, minLen, maxLen):
		if( isinstance(string, str) and len(string) >= minLen and len(string) <= maxLen ):
			return True
		else:
			return False

#########################################################
	def _adjustOpt(self, opt):
		if(not ((opt is not None) and isinstance(opt, dict))):
			raise ChannelException, ('no params are set', Channel.CHANNEL_SDK_PARAM)
		if(not opt.has_key(Channel.TIMESTAMP)):
			opt[Channel.TIMESTAMP] = int(time.time())

		opt[Channel.HOST] = Channel.DEFAULT_HOST 
		opt[Channel.API_KEY] = self._apiKey

		if(opt.has_key(Channel.SECRET_KEY)):
			del opt[Channel.SECRET_KEY]



########################################################
	def _genSign(self, method, url, arrContent):
		gather = method + url
		keys = arrContent.keys()
		keys.sort()
		for key in keys:
			gather += key + '=' + str(arrContent[key])
		gather += self._secretKey
		sign = md5.new(urllib.quote(gather, ''))  #替换'/'
		return sign.hexdigest()


#######################################################3
	def _baseControl(self, opt):
		resource = 'channel'
		if( opt.has_key(Channel.CHANNEL_ID) ):
			if(opt[Channel.CHANNEL_ID] is not None):
				resource = opt[Channel.CHANNEL_ID]
			del opt[Channel.CHANNEL_ID]
		
		host = opt[Channel.HOST]
		del opt[Channel.HOST]
		
		url = 'http://' + host + '/rest/2.0/' + Channel.PRODUCT + '/'
		url += resource
		http_method = 'POST'
		opt[Channel.SIGN] = self._genSign(http_method, url, opt)
		
		request = RequestCore(url)
		headers = dict()
		headers['Content-Type'] = 'application/x-www-form-urlencoded'
		headers['User-Agent'] = 'Baidu Channel Service Pythonsdk Client'

		for (headerKey , headerValue) in headers.items():
			headerValue = headerValue.replace('\r', '')
			headerValue = headerValue.replace('\n', '')
			if (headerValue is not None):
				request.add_header(headerKey, headerValue)
		
		request.set_method(http_method)
		request.set_body(urllib.urlencode(opt))
		
		if(isinstance(self._curlOpts, dict)):
			request.set_curlopts(self._curlOpts)

		request.handle_request()
		return ResponseCore(request.get_response_header(),\
							request.get_response_body(),\
							request.get_response_code())


#######################################################################

	def _commonProcess(self, paramOpt):
		self._adjustOpt(paramOpt)
		ret = self._baseControl(paramOpt)
		if( ret is None):
			raise ChannelException,('base control returned None object', Channel.CHANNEL_SDK_SYS)

		if(ret.isOK()):
			result = json.loads(ret.body)
			if (result is None):
				raise ChannelException, (ret.body, Channel.CHANNEL_SDK_HTTP_STATUS_OK_BUT_RESULT_ERROR)
			self._requestId = result['request_id']
			return result

		result = json.loads(ret.body)
		if(result is None):
			raise ChannelException, ('ret body:' + ret.body, Channel.CHANNEL_SDK_HTTP_STATUS_ERROR_AND_RESULT_ERROR)
		self._requestId = result['request_id']
		raise ChannelException, (result['error_msg'], result['error_code'])


#####################################################33

	def _mergeArgs(self, arrNeed, tmpArgs):
		arrArgs = dict()
		if( len(arrNeed) == 0 and len(tmpArgs) == 0):
			return arrArgs
	
		if(len(tmpArgs)-1 != len(arrNeed) and len(tmpArgs) != len(arrNeed)):
			keys = '('
			for key in arrNeed:
				keys += key + ','
			if(key[-1] == '' and key[-2] == ','):
				keys = keys[0:-2]
			keys += ')'
	
			raise ChannelException, ('invalid sdk, params, params' + keys + 'are need', Channel.CHANNEL_SDK_PARAM)
		if(len(tmpArgs)-1 == len(arrNeed) and tmpArgs[-1] is not None \
			and (not isinstance(tmpArgs[-1], dict)) ):
			raise ChannelException, ('invalid sdk params, optional param must bean array', Channel.CHANNEL_SDK_PARAM)

		idx = 0
		for key in arrNeed:
			if(tmpArgs[idx] is None):
				raise ChannelException, ('lack param' + key, Channel.CHANNEL_SDK_PARAM)
			arrArgs[key] = tmpArgs[idx]	
			idx = idx + 1

		if(len(tmpArgs)  == idx + 1 and tmpArgs[idx] is not None):
			for (key, value) in tmpArgs[idx].items():
				if(not arrArgs.has_key(key) and value is not  None):
					arrArgs[key] = value

		return arrArgs	



		
	
			 


