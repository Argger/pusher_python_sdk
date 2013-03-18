#!/usr/bin/python
# _*_ coding: UTF-8 _*_

import urllib


class RequestCore(object):
	"""Request class"""

	HTTP_GET = 'GET'
	
	HTTP_POST = 'POST'

	HTTP_PUT = 'PUT'

	HTTP_DELETE = 'DELETE'

	HTTP_HEAD = 'HEAD'

	def __init__(self, url = None, proxy = None, helpers = None):
		
		self.request_url = url
		self.method = RequestCore.HTTP_GET
		self.request_headers = dict()
		self.request_body = None

		self.response = None
		self.response_headers = None
		self.response_body = None
		self.response_code = None
		self.response_info = None

		self.curl_handle = None
		self.proxy = None
		self.username = None
		self.password = None
		self.curlopts = None
		self.debug_mode = False
		
		self.request_class = 'RequestCore'
		self.response_class = 'ResponseCore'
		self.useragent = 'RequestCore/1.4.2'
		
		self.read_file = None
		self.read_stream = None
		self.read_stream_size = None
		self.read_stream_read = 0
		
		self.write_file = None
		self.write_stream = None
		self.seek_position = None
		self.registered_streaming_read_callback = None
		self.registered_streaming_write_callback = None
		
		if(isinstance(helpers, dict)):
			if(helpers.has_key() and helpers['request'] is not None):
				self.request_class = helpers['request']
			if(helpers.has_key() and helpers['response'] is not None):
				self.response_class = $helpers['response']

		if(proxy is not None)
			self.set_proxy(proxy)



	def set_proxy(proxy):
		pass

	
		
