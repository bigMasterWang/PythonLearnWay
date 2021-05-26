# -*- coding: utf-8 -*- 
# @Time     : 2021/5/25 19:20 
# @Author   : wangxiaofeng01@corp.netease.com
# @desc:    :


# 描述符拿到属性名字
class Quantity(object):
	_counter = 0

	def __init__(self):
		cls = self.__class__
		self.storage_name = '_{}#{}'.format(cls.__name__, cls._counter)
		cls._counter += 1

	def __get__(self, instance, owner):
		if not instance:
			return self
		else:
			return getattr(instance, self.storage_name)

	def __set__(self, instance, value):
		setattr(instance, self.storage_name, value)


# 类装饰器, 实例化的时候执行, 能获取到属性的名称
def entity(cls):
	for key, attr in cls.__dict__.iteritems():
		if isinstance(attr, Quantity):
			type_name = type(attr).__name__
			attr.storage_name = '_{}#{}'.format(type_name, key)
	return cls


@entity
class LineItem(object):
	desc = Quantity()
	weight = Quantity()
	price = Quantity()

	def __init__(self, desc,  weight, price):
		self.desc = desc
		self.weight = weight
		self.price = price

	def subtotal(self):
		return self.weight * self.price


test = LineItem('123', 1.5, 10)
# print test.subtotal()
# print dir(test)[:2]
print test.desc.storage_name
