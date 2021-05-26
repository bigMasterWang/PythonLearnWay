# -*- coding: utf-8 -*- 
# @Time     : 2021/5/18 22:24 
# @Author   : wangxiaofeng01@corp.netease.com
# @desc:    :


# 使用特性验证属性
# 目前我们只介绍了如何使用@property装饰器实现只读特性.
# 本节要创建一个可读写的特性

class LineItem(object):

	def __init__(self, description, weight, price):
		self.description = description
		self.weight = weight
		self.price = price

	def subtotal(self):
		return self.weight * self.price

	@property
	def weight(self):
		return self.__weight

	@weight.setter
	def weight(self, value):
		if value > 0:
			self.__weight = value
		else:
			raise ValueError('weight muse be > 0')


class TestClass(object):
	data = 'the class data attr'

	@property
	def prop(self):
		return 'the prop value'


# 1. 演示一下实例属性覆盖类的数据属性(覆盖也只是覆盖这个实例的, 不会影响到类本身)
print '=============================================='
obj = TestClass()
# vars()返回实例的__dict__属性, 表明没有实例属性
print vars(obj)
print obj.data
obj.data = 'abc'
print vars(obj)

# 2. 实例属性不会遮盖类的特性
print '=============================================='
print TestClass.prop
print obj.prop
# obj.prop = 1 # AttributeError: can't set attribute

# 新添加的类特性遮盖现有的实例属性 !!!!!!
print '=============================================='
print obj.data
print TestClass.data
TestClass.data = property(lambda self: 'the "data" prop value')
print obj.data
del TestClass.data
print obj.data