# -*- coding: utf-8 -*- 
# @Time     : 2021/1/12 22:00 
# @Author   : wangxiaofeng01@corp.netease.com
# @desc:    :


class MyDecorator(object):

	def __init__(self, func):
		self._func = func

	def __call__(self, *args, **kwargs):
		print '111'
		return self._func(*args, **kwargs)

@MyDecorator
def test_func(x, y=2):
	print x, y

test_func(1)

