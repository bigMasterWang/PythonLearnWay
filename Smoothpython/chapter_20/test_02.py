# -*- coding: utf-8 -*- 
# @Time     : 2021/5/21 17:57 
# @Author   : wangxiaofeng01@corp.netease.com
# @desc:    :


class Quantity(object):

	_counter = 0

	def __init__(self):
		cls = self.__class__
		prefix = cls.__name__
		index = cls._counter
		# 这会造成用户调试困难
		self.storage_name = '_{}#{}'.format(prefix, index)
		cls._counter += 1

	def __get__(self, instance, owner):
		# instance可能为空, 直接通过类调用
		return getattr(instance, self.storage_name)

	def __set__(self, instance, value):
		if value > 0:
			setattr(instance, self.storage_name, value)
		else:
			raise ValueError('value must be > 0')

class QuantityTwo(Quantity):

	def __get__(self, instance, owner):
		if not instance:
			return self
		else:
			return getattr(instance, self.storage_name)


class LineItem(object):

	weight = QuantityTwo()
	price = QuantityTwo()

	def __init__(self, description, weight, price):
		self.description = description
		self.weight = weight
		self.price = price

	def subtotal(self):
		return self.weight * self.price

t1 = LineItem('123', 1.5, 10)
t2 = LineItem('123', 1.5, 20)

print t1.subtotal()
print t2.subtotal()
# print getattr(t1, '_Quantity#0')
# print getattr(t1, '_Quantity#1')

print LineItem.weight



