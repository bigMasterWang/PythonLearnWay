# coding=utf-8
# 第二章 商场促销， 策略模式

# 类的划分是为了封装，继承和多态， 但分类的基础是抽象， 具有相同属性和功能的对象的抽象的抽象集合才是类
# 所以并不是类越多越好

# 策略模式： 定义了算法的集合，他们之间可以互相替换，此模式让算法的变化不会影响到使用算法的客户

# 用策略模式重写计算器

import abc


class Operation(object):
	
	@abc.abstractmethod
	def get_result(self, a, b):
		pass


class AddOperation(Operation):
	def get_result(self, a, b):
		return a + b


class SubOperation(Operation):
	def get_result(self, a, b):
		return a - b


class MulOperation(Operation):
	def get_result(self, a, b):
		return a * b


class DivOperation(Operation):
	def get_result(self, a, b):
		return a / b


# 也就是说工厂模式是传入参数返回类
# 而策略模式传入参数就返回这个策略集合类本身， 然后再写一个统一的返回结果的方法
# 至于用哪一个策略（或者工厂模式的哪个类，外界并不用知道， 只用这个上下文类获取结果就行了）
class OperationContext(object):
	
	def __init__(self, operation):
		if operation == '+':
			self.op = AddOperation()
		if operation == '-':
			self.op = SubOperation()
		if operation == '*':
			self.op = MulOperation()
		if operation == '/':
			self.op = DivOperation()
	
	def get_result(self, a, b):
		return self.op.get_result(a, b)


class OperationFactory(object):
	
	@staticmethod
	def get_operation(operation):
		if operation == '+':
			return AddOperation()
		if operation == '-':
			return SubOperation()
		if operation == '*':
			return MulOperation()
		if operation == '/':
			return DivOperation()


def get_input():
	number_a = int(raw_input('please input number a\n'))
	number_b = int(raw_input('please input number b\n'))
	operation = raw_input('please input operation +-*/\n')
	return operation, number_a, number_b


def test_01():
	operation, x, y = get_input()
	# 外界需要知道工厂类 和 工厂里面返回的这个类的用法
	op = OperationFactory.get_operation(operation=operation)
	print op.get_result(x, y)


def test_02():
	operation, x, y = get_input()
	# 策略模式只需要知道策略类， 其实就是工厂策略的升级版
	# 用户只需要知道工厂类， 以及工厂类里面的获取结果的党法
	op = OperationContext(operation)
	print op.get_result(x, y)


if __name__ == '__main__':
	# test_01()
	test_02()
