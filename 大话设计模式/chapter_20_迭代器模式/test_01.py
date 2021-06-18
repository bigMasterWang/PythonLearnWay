# -*- coding: utf-8 -*-
# @Time     : 2021/6/15 19:41
# @Author   : wangxiaofeng01@corp.netease.com
# @desc:    : 第二十章 想走?可以!先买票——迭代器模式

# python中已经实现了迭代器模式, 但是不妨把迭代器地结构写一下

# 结构:
from abc import ABC, abstractmethod


class MyIterator(ABC):

	@abstractmethod
	def first(self):
		pass

	@abstractmethod
	def next(self):
		pass

	@abstractmethod
	def current_item(self):
		pass

	@abstractmethod
	def is_done(self):
		pass


class Aggregate(ABC):

	@abstractmethod
	def create_iterator(self):
		pass


class ConcreteIterator(MyIterator):
	def __init__(self, _aggregate):
		self.aggregate = _aggregate
		self.current_index = 0

	def first(self):
		return self.aggregate[0]

	def next(self):
		self.current_index += 1
		if self.current_index < len(self.aggregate):
			return self.current_item()

	def current_item(self):
		return self.aggregate[self.current_index]

	def is_done(self):
		return True if self.current_index >= len(self.aggregate) else False


class ConcreteAggregate(Aggregate):
	def __init__(self):
		self.content = range(1, 10, 1)

	def create_iterator(self):
		return ConcreteIterator(self.content)


ca = ConcreteAggregate()
ct = ca.create_iterator()

print(ct.first())
while not ct.is_done():
	print(ct.next())


# 但是python中只要实现几个方法就行了, 如__getitem__
class MyQueue:

	def __init__(self):
		self.content = range(1, 10)

	def __getitem__(self, _index):
		return self.content[_index]


x = MyQueue()
for item in x:
	print(item)