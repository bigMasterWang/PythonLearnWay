# coding=utf-8
# 第六章,穿什么有这么重要?----装饰模式

import abc


# 结构展示
class FatherClass(object):
	
	@abc.abstractmethod
	def operation(self):
		pass


class TargetClass(FatherClass):
	def operation(self):
		print 'I am target class'


class DecoratorClass(FatherClass):
	
	def __init__(self):
		self.my_target = None
	
	def set_target(self, target):
		self.my_target = target
	
	def operation(self):
		if self.my_target:
			self.my_target.operation()


class DecoratorA(DecoratorClass):
	
	def operation(self):
		print 'this is {}'.format(self.__class__.__name__)
		super(DecoratorA, self).operation()


class DecoratorB(DecoratorClass):
	
	def operation(self):
		print 'this is {}'.format(self.__class__.__name__)
		super(DecoratorB, self).operation()


a = TargetClass()
d1 = DecoratorA()
d2 = DecoratorB()

d1.set_target(a)
d2.set_target(d1)
d2.operation()


# 装饰模式就是这么个结构, 一个全部的父类, 客户类继承父类, 修饰类也继承父类
# 并且修饰类内部声明一个父类的变量, 然后父类因为有一个抽象的执行方法,那么装饰类
# 和客户类的执行方法一致

# 如果没有FatherClass, 那么修饰类可以是TargetClass目标类的子类,
# 并且修饰类也没有必要有一个抽象的父类, 主要是想用同一个set_target的方法
# 总之就是如果想修饰一个类, 那就弄一个和这个类的类型一样的修饰类, 修饰类中
# 声明一个这个类的变量就行了

# 精简版

class Target(object):
	
	def operation(self):
		print 'I am {}'.format(self.__class__.__name__)


class Decorator(Target):
	
	def __init__(self):
		self.target = None
		
	def set_target(self, target):
		self.target = target
		
	def operation(self):
		if self.target:
			print '=================================================='
			print 'Decorator {} start'.format(self.__class__.__name__)
			self.target.operation()
			print 'Decorator {} end'.format(self.__class__.__name__)


t = Target()
d = Decorator()
d.set_target(t)
d.operation()

# 目的是什么呢?
# 把类中的装饰功能从类中搬移出去,这样可以简化原有的类
# 有效的把类的核心职责和装饰功能区分开了,而且可以去除相关类中的重复逻辑
