# -*- coding: utf-8 -*- 
# @Time     : 2021/3/30 9:38 
# @Author   : wangxiaofeng01@corp.netease.com
# @desc:    :
import datetime
import random
import time

# least recently, used
class MyLruCache(object):

	def __init__(self, size):
		super(MyLruCache, self).__init__()
		self.cache = {}
		self.max_cache_size = size

	def __contains__(self, item):
		return item in self.cache

	def get_cache_size(self):
		return self.max_cache_size

	def update_cache(self, key, value):
		# 加入新的, 但是缓存已经满了
		if key not in self.cache and self.max_cache_size <= len(self.cache):
			self.remove_oldest()
		self.cache[key] = {'data': time.time(), 'value': value}

	def remove_oldest(self):
		oldest = None
		for k in self.cache:
			if not oldest:
				oldest = k
			elif self.cache[k]['data'] < self.cache[oldest]['data']:
				oldest = k
		self.cache.pop(oldest)

# from collections import OrderedDict
# OrderedDict.popitem(last=False) 队列, 弹出最先插入的
# OrderedDict.popitem(last=True) 堆栈, 弹出最近插入

if __name__ == "__main__":
	keys = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
	cache = MyLruCache(5)
	for i, key in enumerate(keys):
		if key in cache:
			continue
		else:
			cache.update_cache(key, key)
	for i in cache.cache.iteritems():
		print i