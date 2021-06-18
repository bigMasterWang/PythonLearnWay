# -*- coding: utf-8 -*-
# @Time     : 2021/6/17 21:02
# @Author   : wangxiaofeng01@corp.netease.com
# @desc:    : 第22章, 手机软件何时同意——桥接模式


# 对象的继承关系是在编译时就定义好了, 所以无法在运行时改变从父类继承的实现.
# 子类的实现与它的父类又非常紧密的依赖关系, 以至于父类实现中的任何变化必然会导致子类发生变化
# 当你需要复用子类时, 如果继承下来的实现不适合解决新的问题, 则父类必须重写或被其他更适合的
# 类替换. 这种依赖关系限制了灵活性并最终限制了复用性

# 优先使用对象合成/聚合, 而不是类继承
# 合成/聚合复用原则: 尽量使用合成/聚合, 尽量不要使用类继承

# 聚合表示一种弱的'拥有'关系, 体现的是A对象可以包含B对象, 但B对象不是A对象的一部分
# 合成则是一种强的'拥有'关系, 体现了严格的部分和整体的关系, 部分和整体的生命周期一样
# 翅膀   ---合成--->   大雁   ---聚合--->   雁群

# 桥接模式: 将抽象部分与它的实现部分分离, 使它们都可以独立地变化
# 			实现系统可能多角度分类, 每一种分类都有可能变化, 那么久吧这种多角度分离出来让他们独立变化, 减少
# 			它们之间的耦合
# 结构:
from abc import ABC, abstractmethod


class Implementor(ABC):

	@abstractmethod
	def operation(self):
		pass


class ConcreteImplementorA(Implementor):

	def operation(self):
		print('具体实现A的方法执行')


class ConcreteImplementorB(Implementor):
	def operation(self):
		print('具体实现B的方法执行')


class Abstraction(ABC):
	def __init__(self):
		self.implementor = None

	def set_implementor(self, _implementor):
		self.implementor = _implementor

	@abstractmethod
	def operation(self):
		self.implementor.operation()


class ConcreteAbstraction(Abstraction):

	def operation(self):
		self.implementor.operation()


# 桥接模式地核心意图就是把这些实现独立出来, 让他们各自地变化, 这就使得每种实现地变化不会影响其他实现, 从而达到应对变化地目的
def test_01():
	ab = ConcreteAbstraction()
	ab.set_implementor(ConcreteImplementorA())
	ab.operation()

	ab.set_implementor(ConcreteImplementorB())
	ab.operation()


# 着看着也太抽象了, 看看具体的例子吧
# 手机中有不同的软件(通讯录, 游戏, mp3等), 还有品牌等等
# 怎么写一个手机类呢??
# 下意识地面向对象的想法肯定是:
# 1. 建立一个抽象的手机类, 然后每个手机都有自己的软件属性, 还有牌子, 这样无论是增加手机牌子还是软件, 都非常非常麻烦
# 但是这样做不是很好
# 应该是 软件  ---聚合---> 手机


class PhoneSoft(ABC):

	@abstractmethod
	def run(self):
		pass


class Game(PhoneSoft):

	def run(self):
		print('运行游戏')


class Mp3(PhoneSoft):

	def run(self):
		print('运行mp3')


class PhoneBrand(ABC):

	def __init__(self):
		self.soft = None

	def set_soft(self, _soft):
		self.soft = _soft

	@abstractmethod
	def run(self):
		self.soft.run()


class XiaoMi(PhoneBrand):

	def run(self):
		self.soft.run()


class HuaWei(PhoneBrand):

	def run(self):
		self.soft.run()

# 这样无论是增加软件还是手机品牌都很方便
# 甚至set_phone可以改成add_phone, soft变成list即可
def test_02():
	xm = XiaoMi()
	xm.set_soft(Game())
	xm.run()
	xm.set_soft(Mp3())
	xm.run()

	hw = HuaWei()
	hw.set_soft(Game())
	hw.run()
	hw.set_soft(Mp3())
	hw.run()


if __name__ == '__main__':
	# test_01()
	test_02()