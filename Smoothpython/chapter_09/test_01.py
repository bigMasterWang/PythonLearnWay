# -*- coding: utf-8 -*- 
# @Time     : 2021/4/15 21:14 
# @Author   : wangxiaofeng01@corp.netease.com
# @desc:    : 符合Python风格的对象
"""绝对不要使用两个前导下划线, 这是很烦人的自私行为"""
#  本章接续第一章, 说明如何是现在很多Python类型中常见的特殊方法


"""
repr() : 以便于开发者理解的方式返回对象的字符串表示形式
str()  : 以便于用户理解的方式返回对象的字符串表示形式
只要实现 __repr__, __str__即可, 并且还会用到另外两个特殊方法: __bytes__, __format__
过程中学习 
1. @classmethod, @staticmethod的用法
2. Python的私有属性和受保护属性的用法, 约定和局限
"""
import inspect

def whoami():
	return inspect.stack()[1][3]

def whosdaddy():
    return inspect.stack()[2][3]


class Vector2d:

	def __init__(self, x, y):
		self.x = float(x)
		self.y = float(y)

	def __iter__(self):
		"""
		inspect.stack()中的数组, 自己, 上一层, 上一层,,,,
		用法: x, y = v1, 执行拆包时用, 循环时也用
		__iter__要求返回一个generator, 而不是tuple
		"""
		print inspect.stack()[0][3]
		# return (self.x, self.y)
		return (i for i in (self.x, self.y))

	def __repr__(self):
		"""
		type:
		"""
		class_name = type(self).__name__
		return '{}({!r}, {!r})'.format(class_name, *self)

	def __str__(self):
		"""
		tuple(self)是什么???
		"""
		return str(tuple(self))

	def __eq__(self, other):
		"""
		???
		"""
		return tuple(self) == tuple(other)

	def __abs__(self):
		import math
		return math.hypot(self.x, self.y)

	def __bool__(self):
		return bool(abs(self))




v1 = Vector2d(3, 4)
v2 = Vector2d(3, 4)
print v1 == v2

# classmethod 与 staticmethod
"""
classmethod装饰器非常有用, 但是作者从未见过不得不用staticmethod的情况.如果想定义不需要与类交互的函数,那么在模块中定义就好了.
有时,函数虽然从不处理类, 但是函数的功能与类紧密相关,因此想把它放在近处. 即便如此,在同一模块中的类前面或后面定义函数也就行了
"""
class Demo(object):

	@classmethod
	def klassmeth(cls, *args):
		print cls.__name__
		return args

	@staticmethod
	def statmeth(*args):
		return args

print Demo.klassmeth()
print Demo.statmeth()

# 9.5 格式化显示
brl = 1/2.43
print brl
print format(brl, '0.4f')
print '1 BRL = {rate:0.2f} USD'.format(rate=brl)
# 格式规范语言为一些内置类型提供了专用的表示代码,比如b和x分别表示二进制和十六进制
print format(42, 'b')
print format(2.0/3.0, '.1%')
print format(17, 'x')
# 格式规范语言是可扩展的, 因为各个类可以自行决定如何解释format_spec参数. 例如datetime模块中的类
from datetime import datetime
now = datetime.now()
print format(now, '%Y年%m月%d日  %H时%M分%S秒')
# 如果类没有定义__format__方法, 那么从object继承的方法
print format(v1)
# 然而传入格式说明符, object.__format__方法会抛出TypeError


class NewVector2(Vector2d):

	def __format__(self, fmt_spec=''):
		# 调用了__iter__, for循环self调用的就是类/实例里面的__iter__
		properties = (format(c, fmt_spec) for c in self)
		print properties
		return '{}. {}'.format(*properties)

v3 = NewVector2(1, 3)
print format(v3, '.3e')


class NewVector3(Vector2d):

	def angle(self):
		import math
		return math.atan2(self.y, self.x)

	# 带极坐标
	def __format__(self, fmt_str=''):
		if fmt_str.endswith('p'):
			fmt_str = fmt_str[:-1]
			coords = (abs(self), self.angle())
			outer_fmt = '<{}, {}>'
		else:
			coords = self
			outer_fmt = '({}, {})'
		# properties = (format(c, fmt_str) for c in coords)
		properties = (c for c in coords)
		return outer_fmt.format(*properties)

v4 = NewVector3(10, 10)
print format(v4, 'p')
print format(v4)












