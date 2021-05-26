# -*- coding: utf-8 -*- 
# @Time     : 2021/1/12 21:22 
# @Author   : wangxiaofeng01@corp.netease.com
# @desc:    :
"""单派分函数对比"""

def sigle_dispatch(func):

	funcs = {}

	def register(type):
		# 返回一个修饰器
		def dispatched_decorator(execute_func):
			def _inner(*args, **kwargs):
				print type
				return execute_func(*args, **kwargs)
			return _inner
		return dispatched_decorator

	def inner(*args, **kwargs):
		print '我执行了???'
		return funcs[type(args[0])](*args, **kwargs)

	setattr(inner, 'register', register)
	return inner


# 第一遍给被修饰的函数添添加上register注册函数
# 为什么inner()函数中没有执行func? 反正我们最后真正执行的也不是这个process_type()
# 而是我们的process_type.register注册的函数, 所以里面执行的是funcs[type(args[0])](*args, **kwargs)
# 最后执行的是process_type()看清楚
@sigle_dispatch
def process_type(obj):
	return 'this is obj'

@process_type.register(str)
def xxx(text):
	print 'this is string'
	return 'xxx'

@process_type.register(int)
def yyy(num):
	print 'this is int'
	return 'yyy'

print xxx(1)
print xxx('test')
print yyy(2)
