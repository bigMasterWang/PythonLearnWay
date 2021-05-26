# -*- coding: utf-8 -*- 
# @Time     : 2021/5/20 21:21 
# @Author   : wangxiaofeng01@corp.netease.com
# @desc:    : 第20章, 属性描述符


# 描述符类
class Quantity(object):

	def __init__(self, storage_name):
		self.storage_name = storage_name

	def __set__(self, instance, value):
		if value > 0:
			instance.__dict__[self.storage_name] = value
		else:
			raise ValueError('value must be > 0')

class LineItem(object):

	# 想一想怎么把Quantity去掉呢??
	weight = Quantity('weight')
	price = Quantity('price')

	def __init__(self, description, weight, price):
		self.description = description
		self.weight = weight
		self.price = price

	def subtotal(self):
		return self.weight * self.price

x = LineItem('we', 10, 1.5)
print x.weight
x.weight = 15
print x.weight

