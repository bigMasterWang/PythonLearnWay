# -*- coding: utf-8 -*- 
# @Time     : 2021/1/11 19:54 
# @Author   : wangxiaofeng01@corp.netease.com
# @desc:    :
"""一个新的装饰器, 使用了functools.warps"""
import time
import functools


def clock(func):
	# 协助构建行为良好的装饰器
	# 主要是用来保证被修饰的方法的名称等属性保持不变
	functools.wraps(func)

	def inner(*args, **kwargs):
		start_time = time.time()
		result = func(*args, **kwargs)
		end_time = time.time()

		func_name = func.__name__
		args_list = []
		if args:
			args_list.append(','.join(repr(arg) for arg in args))
		if kwargs:
			pairs = [str(k) + ':' + str(w) for k, w in kwargs.items()]
			args_list.append(','.join(pairs))
		print 'run time: ' + str(end_time - start_time), 'name: ' + func_name, 'args: ', ','.join(args_list)
		return result
	return inner


@clock
def test_func(run_times, cnmd):
	timer = 1
	while True:
		time.sleep(1)
		timer += 1
		if timer > run_times:
			break


# test_func(5, cnmd='waedwa')


# functools.lru_Cache(leaest recent userd)
# 但是python2中没有functools.lru_cache
# 所以我们手动实现一个, 老牛逼了
def my_cache(func):
	cache_dict = {}
	def inner(*args, **kwargs):
		if args in cache_dict.keys():
			return cache_dict[args]
		result = func(*args, **kwargs)
		cache_dict[args] = result
		return result

	return inner


@my_cache
@clock
def fibonacci(n):
	if n < 2:
		return n
	return fibonacci(n-2) + fibonacci(n-1)


print fibonacci(22)
