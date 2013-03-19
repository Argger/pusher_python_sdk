#!/usr/bin/python
# _*_ coding: UTF-8 _*_

import urlparse
import pycurl
import StringIO


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
				self.response_class = helpers['response']

		if(proxy is not None):
			self.set_proxy(proxy)


	def __del__(self):
		if(self.read_file is not None and self.read_stream is not None):
			self.read_stream.close()
		if(self.write_file is not None and self.write_stream is not None):
			self.write-stream.close()
		
	def set_credentials(self, username, password):
		self.username = username
		self.password = password

	def add_header(self, key, value):
		self.request_headers[key] = value

	def remove_header(self, key):
		if(self.request_headers.has_key(key)):
			del self.request_headers[key]

	def set_method(self, method):
		self.method = method.upper()

	def set_useragent(self, ua):
		self.useragent = ua

	def set_body(self, body):
		self.request_body = body

	def set_request_url(self, url):
		self.request_url = url
	
	def set_curlopts(self, curlopts):
		self.curlopts = curlopts

	def set_read_stream_size(self, size):
		self.read_stream_size = size

	def set_read_stream(self, resource, size = None):
		pass

	def set_read_file(self, location):
		pass

	def set_write_stream(self, resource):
		pass

	def set_write_file(self, location):
		pass

	def set_proxy(self, proxy):
		self.proxy = urlparse.urlparse(proxy)

	def set_seek_position(self, position):
		pass
	
	def register_streaming_read_callback(self, callback):
		self.registered_streaming_read_callback = callback

	def register_streaming_write_callback(self, callback):
		self.registered_streaming_write_callback = callback

	def streaming_read_callback(self, curl_handle, file_handle, length):
		if (self.read_stream_read >= self.read_stream_size):
			return None
		if(self.read_stream_read == 0 and self.seek_position and \
			self.seek_position != self.read_stream.tell()):
			self.read_stram.seek(self.seek_postion)
		if(self.seek_position != self.read_stream.tell()):
			raise RequestCore_Exeption,('The stream does not support seeking and is either not at the requested position or the position is unknown.')
		
		read = self.read_stream.read(min(self.read_stream_size - self.read_stream_read, length))
		self.read_stream_read += len(read)
		out = read

		if(self.registered_streaming_read_callback):
			self.call_user_func(self.registered_streaming_read_callback, curl_handle, file_handle, out)

		return out
		
		 	
	def stream_write_callback(self, curl_handle, data):
		length = len(data)
		written_last = 0
		self.write_stream.write(data)
		self.write_stream.flush()
		if(self.registered_streaming_write_callback):
			call_user_func(self.registered_streaming_write_callback, curl_handle, length)
		return length
		

	def prep_request(self):
		curl_handle = pycurl.Curl()
		# set default options.
		curl_handle.setopt(pycurl.URL, self.request_url)
		curl_handle.setopt(pycurl.REFERER, self.request_url)
		curl_handle.setopt(pycurl.USERAGENT, self.useragent)
		curl_handle.setopt(pycurl.TIMEOUT, 5184000)
		curl_handle.setopt(pycurl.CONNECTTIMEOUT, 120)
		curl_handle.setopt(pycurl.HEADER, True)
		curl_handle.setopt(pycurl.VERBOSE, 1)
		curl_handle.setopt(pycurl.FOLLOWLOCATION, 1)
		curl_handle.setopt(pycurl.MAXREDIRS, 5)
		if(self.request_headers and len(self.request_headers) > 0):
			curl_handle.setopt(pycurl.HTTPHEADER, 'xxxxxx')
		#if(self.method == self.HTTP_PUT):
		curl_handle.setopt(pycurl.POSTFIELDS, self.request_body)
		curl_handle.fp = StringIO.StringIO()
		curl_handle.setopt(pycurl.WRITEFUNCTION, curl_handle.fp.write)
		return curl_handle


	def send_request(self, parse = False):
		curl_handle = self.prep_request()
		self.response = curl_handle.perform()
		print self.response
