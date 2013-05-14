Baidu Push 服务器端SDK Python版

==============
Python SDK总体介绍：
将百度Push服务端的所有操作封装成一个类Channel，通过对该类的简单初始化，即可调用其内部的各种方法，使用百度Push服务。
Channel提供的方法和服务端API对应，是对服务端REST API的封装，REST API请参考:http://developer.baidu.com/wiki/index.php?title=docs/cplat/push/api/list  
使用前提:
支持pycurl的python版本

工具组成：
Python SDK工具包主要由以下部分组成：
	Channel.py -- Python_SDK 脚本，包含对外提供的所有接口
	lib -- 使用到的一些基础公用文件
	sample/sample.python -- 展示如何使用 Python_SDK 的 demo 文件

SDK 依赖于以下组件：
	pycurl
	python


一般规则
	所有函数的参数和返回值中如果有中文，必须是UTF-8编码；
	不需要对函数参数进行urlencode。
错误码集合
如果用户在调用SDK时发生错误，那么错误分成两大类：
	与服务交互失败产生的错误，比如：SDK参数不完整、网络错误、服务器的返回不是正确的json包导致无法解析等，这类错误的错误码位于1-100区间，具体如下：
服务器交互失败错误
错误码	错误信息
1	python sdk error
2	Python sdk init error
3	lack param
4	http status is error, and the body returned is not a json string
5	http status is ok, but the body returned is not a json string

	与服务器交互成功，但服务器返回了非200的HTTP状态，比如用户权限错误、重复绑定等，具体如下：
HTTP状态错误
错误码	错误信息
30600	Internal Server Error
30601	Method Not Allowed
30602	Request Params Not Valid
30603	Authentication Failed
30604	Quota Use Up Payment Required
30605	Data Required Not Found
30606	Request Time Expires Timeout
30607	Channel Token Timeout
30608	Bind Relation Not Found
30609	Bind Number Too Many
30610	Duplicate Operation
