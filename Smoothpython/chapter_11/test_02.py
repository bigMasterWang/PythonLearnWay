# -*- coding: utf-8 -*- 
# @Time     : 2021/5/7 21:52 
# @Author   : wangxiaofeng01@corp.netease.com
# @desc:    :

# 抽象基类的数字塔
import numbers

# Number <- Complex <- Real <- Rational <- Integral
# Integral : int , bool
# Real : bool, int, float, fractions.Fraction
print(isinstance(1, numbers.Rational))

# 我们将从零开始实现一个抽象基类, 然后实际使用, 以此实践白鹅类型
# 随机广告类 ADAM
# 1. 支持用户提供随机挑选的无重复类
# 		两个抽象方法
# 		.load(): 把元素放入容器
# 		.pick(): 从容器中随即拿出一个元素, 返回选中的元素
# 		两个具体方法
#		.loaded(): 如果容器中至少有一个元素, 返回True
# 		.inspect(): 返回一个有序元组, 由容器中的现有元素构成, 不会修改容器的内容

import abc


# 抽象基类, 继承abc.ABC
class Tombola(object):

	__metaclass__ = abc.ABCMeta

	@abc.abstractmethod
	def load(self, iterable):
		"""从可迭代对象中添加元素"""

	@abc.abstractmethod
	def pick(self):
		"""随机删除元素, 并将其返回,
		如果实例为空, 这个方法应抛出'LookupError'
		"""

	def loaded(self):
		"""如果至少有一个元素, 返回'True'. 否则返回'False'"""
		return bool(self.inspect())

	def inspect(self):
		"""返回一个有序元组, 由当前元素构成"""
		items = []
		while True:
			try:
				items.append(self.pick())
			except LookupError:
				break
		self.load(items)
		return tuple(sorted(items))


class Test(Tombola):

	def pick(self):
		return 23


a = Test()
# python3下直接报错: TypeError: Can't instantiate abstract class Test with abstract methods load
# python2下虽然有@abc.abstractmethod修饰器, 但是不会报错

# 两个子类
import random
class BingpCage(Tombola):
	# 继承了Tombola的臃肿的inspect和loaded方法
	def __init__(self, items):
		self._randomizer = random.SystemRandom()
		self._items = []
		self.load(items)

	def load(self, iterable):
		self._items.extend(iterable)
		self._randomizer.shuffle(self._items)

	def pick(self):
		try:
			return self._items.pop()
		except IndexError:
			raise LookupError('pick from empty BingoCage')

	def __call__(self, *args, **kwargs):
		self.pick()

class LotteryBlower(Tombola):

	def __init__(self, iterable):
		# 使用list(), 不改变原来的
		self._balls = list(iterable)

	def load(self, iterable):
		self._balls.extend(iterable)

	def pick(self):
		try:
			position = random.randrange(len(self._balls))
		except:
			raise LookupError('pick from empty LotteryBlower')
		return self._balls.pop(position)

	def loaded(self):
		return bool(self._balls)

	def inspect(self):
		return tuple(sorted(self._balls))

# 白鹅类型: 即便不继承, 也有办法把一个类注册为抽象基类的虚拟子类
# 		注册虚拟子类的方式是在抽象基类上调用register方法, issubclass, isinstance都可以用
# 		但是注册的类不会从抽象基类中继承任何方法或者属性

# 虚拟子类
from random import randrange

class TomoList(list):

	def pick(self):
		if self:
			position = randrange(len(self))
			return self.pop(position)
		else:
			raise LookupError('pop from empty TomboList')

	# 这句话牛逼了
	load = list.extend

	def loaded(self):
		return bool(self)

	def inspect(self):
		return tuple(sorted(self))

# Tombola.register(TomoList) python2好像不太行
# python风格就是鸭子类型, 更甚者白鹅类型(抽象基类, 甚至不需要继承, 只需要注册)

# 强类型: 很少使用隐式转换 python, C++, Java
# 弱类型: 经常使用隐士转换 JavaScript, PHP, Perl
# 静态类型: 编译时检查类型的语言 C++, Java
# 动态类型: 运行时检查类型的语言 Python

# 猴子补丁???