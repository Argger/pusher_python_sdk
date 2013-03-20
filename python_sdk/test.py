#!/usr/bin/python

from Channel import *

accessKey = 'GkWwrvZrCaMQfCZ190ujndZm'
secretKey = 'I5nqT2szvC12Qdf1gHZ5RSpPnluVo4VI'

user_id = '580118370301074982'
channel_id = '3915728604212165383'

c = Channel(accessKey, secretKey)
ret = c.queryBindList(user_id)

print ret
type(ret)
"""
arrContent = {'name':'liu', 'age':23}
print c._genSign('POST', 'www.baidu.com', arrContent)

arrNeed = ['name', 'age']
tmpargs = ['liu', 23, {'school':'nju', 'addr':'bj'}]
opt = c._mergeArgs(arrNeed, tmpargs)

c._adjustOpt(opt)
print opt
"""
