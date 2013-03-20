#!/usr/bin/python

class ChannelException(Exception):
	def __init__(self, error_msg, error_id):
		self.error_msg = error_msg
		self.error_id = error_id
