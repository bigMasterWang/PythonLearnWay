# -*- coding: utf-8 -*- 
# @Time     : 2021/1/11 20:42 
# @Author   : wangxiaofeng01@corp.netease.com
# @desc:    :
"""单派分函数"""

def sigle_dispatch(func):

	funcs = {}

	def register(type):
		# 里面这个返回的时一个修饰器, 是不是? 这就是关键
		# 但是这个单派分又不执行里面的函数, 所以就没有在里面进一步的写参数, 的_inner, 我们
		# 马上做一个丢彼
		def _inner(execute_func):
			funcs[type] = execute_func
		return _inner

	# 这个参数是执行时的概念, 只有执行的时候才知道参数
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
	return text

@process_type.register(int)
def yyy(num):
	print 'this is int'
	return num

print process_type(1)
print process_type('test')
print process_type(2)

# 所以理解decorator:
# 1. 修饰器外层默认接收一个参数, 就是这个方法
# 2. 里面的函数, 接收到的参数, 是一个运行时的概念, 因为返回的是里面的函数, 所以函数函数运行的时候
#		里面的函数将接收到修饰器所修饰的函数的参数, 其实就根本没有2, 修饰器原本上的概念就仅仅只是
#		python把被装饰的函数作为第一个参数传递给装饰器函数, 至于返回什么函数, 自己随意
