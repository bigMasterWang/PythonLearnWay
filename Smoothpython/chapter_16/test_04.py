# -*- coding: utf-8 -*- 
# @Time     : 2021/5/12 20:30 
# @Author   : wangxiaofeng01@corp.netease.com
# @desc:    :

# 让协程最终返回一个值

from collections import namedtuple
from functools import wraps
Result = namedtuple('result', 'total count')

def my_coroutine(func):
	@wraps(func)
	def inner():
		gen = next(func)
		return gen
	return inner

# pyhton 3.3之前版本generator不允许return
@my_coroutine
def my_averager():
	total = 0.0
	count = 0
	while True:
		number = yield
		total += number
		count += 1
	# return Result(total, count)

x = my_averager()
x.send(1)
x.send(2)
x.send(3)
x.send(4)
try:
	x.send(None)
except StopIteration as e:
	# 如果可以return的话, 那么返回值会在异常的value属性里面
	print e.value