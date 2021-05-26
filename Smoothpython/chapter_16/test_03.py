# -*- coding: utf-8 -*- 
# @Time     : 2021/5/12 20:04 
# @Author   : wangxiaofeng01@corp.netease.com
# @desc:    :

# 终止协程和异常处理

class DemoExeption(Exception):
	"""自定义异常"""


def demo_exc_handing():
	while True:
		try:
			x = yield
		except DemoExeption:
			print DemoExeption.__class__.__name__
		else:
			print 'coroutine received x:', x
	raise RuntimeError('this line should never run.')


my_exc_coro = demo_exc_handing()
next(my_exc_coro)
my_exc_coro.send(1)
my_exc_coro.send(2)
my_exc_coro.send(3)
my_exc_coro.send(4)
# 上面的coroutine如果接收到了没有处理的异常, 协程就会终止
my_exc_coro.throw(DemoExeption)

# 如果写成无论如何都想做些清理工作, 那么要把写成定义体中相关的代码放入try/finally块中

def demo_finally():
	try:
		while True:
			try:
				x = yield
			except DemoExeption:
				print DemoExeption.__name__
			else:
				print 'coroutine received x:', x
	finally:
		print 'coroutine ending'

test_coro = demo_finally()
next(test_coro)
test_coro.send(1)
test_coro.send(2)
test_coro.send(3)
test_coro.send(4)
test_coro.send(ZeroDivisionError)

