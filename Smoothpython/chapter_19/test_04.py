# -*- coding: utf-8 -*- 
# @Time     : 2021/5/20 20:34 
# @Author   : wangxiaofeng01@corp.netease.com
# @desc:    : 定义一个特性工厂函数




def quantity(storage_name):

	def qty_getter(instance):
		return instance.__dict__[storage_name]

	def qty_setter(instance, value):
		if value > 0:
			instance.__dict__[storage_name] = value
		else:
			raise ValueError('value must be > 0')

	return property(qty_getter, qty_setter)

class LineItem(object):

	weight = quantity('weight')
	price = quantity('price')

	def __init__(self, description, weight, price):
		self.description = description
		self.weight = weight
		self.price = price

	def subtotal(self):
		return self.weight * self.price

# a = LineItem('123', 0, 2) # ValueError: value must be > 0
b = LineItem('ewafw', 1.5, 10)
print b.subtotal()

# 通过特性删除属性
class DeleteClass(object):

	def __init__(self, weight, price):
		self.weight = weight
		self.price = price

	@property
	def weight(self):
		return self._weight

	@weight.setter
	def weight(self, value):
		self._weight = value

	# property(setter, getter, deleter , doc)
	@weight.deleter
	def weight(self):
		del self._weight
		print '?????'

x = DeleteClass(1, 2)
del x.weight


