#!/usr/bin/python

from Channel import *

accessKey = 'aaaaaaaaaaaaaaaaaaaaaa'
secretKey = 'sssssssssssssssssssssssss'

c = Channel(accessKey, secretKey)

print c._accessKey
print c._secretKey

arrContent = {'name':'liu', 'age':23}
print c._genSign('POST', 'www.baidu.com', arrContent)

arrNeed = ['name', 'age']
tmpargs = ['liu', 23, {'school':'nju', 'addr':'bj'}]
opt = c._mergeArgs(arrNeed, tmpargs)

c._adjustOpt(opt)
print opt

