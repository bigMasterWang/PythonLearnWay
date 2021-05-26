# -*- coding: utf-8 -*- 
# @Time     : 2021/5/12 18:19 
# @Author   : wangxiaofeng01@corp.netease.com
# @desc:    :

# 示例, 使用写成计算移动平均值
def averager():
	total = 0.0
	count = 0
	average = None
	while True:
		term = yield average
		total += term
		count += 1
		average = total / count


my_averager = averager()
next(my_averager)

print my_averager.send(1)
print my_averager.send(2)
print my_averager.send(3)
print my_averager.send(4)

# 预激协程的装饰器
from functools import wraps


def coroutine(func):
	@wraps(func)
	def primer(*args, **kwargs):
		gen = func(*args, **kwargs)
		next(gen)
		return gen

	return primer

@coroutine
def my_test_coroutine():
	count = 0
	total = 0.0
	average = None
	while True:
		number = yield average
		count += 1
		total += number
		average = total / count

my_averager_2 = my_test_coroutine()
print my_averager_2.send(1)
print my_averager_2.send(2)
print my_averager_2.send(3)
print my_averager_2.send(4)