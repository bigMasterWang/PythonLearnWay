# -*- coding: utf-8 -*- 
# @Time     : 2021/1/12 21:33 
# @Author   : wangxiaofeng01@corp.netease.com
# @desc:    :

"""带参数的修饰器"""
# 实际上就是像装饰器的那个函数返回一个装饰器罢了


def test_decorator(active=True):
	def real_decorator(func):
		def execute_func(*args, **kwargs):
			if active:
				func(*args, **kwargs)
			else:
				print '选择不执行'
		return execute_func
	return real_decorator


@test_decorator(active=True)
def print_hello(x):
	print x


@test_decorator(active=True)
def print_world(y):
	print y


print_hello('hello')
print_world('world')