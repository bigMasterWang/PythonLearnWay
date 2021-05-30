# 雷锋依然在人间——工厂方法模式

# 工厂方法模式：定义一个用于创建对象的接口，让子类决定实例化哪一个类
# 工厂方法使一个类的实例化延迟到其子类


# 我的想法：
# 1.工厂方法模式确实让简单工厂模式符合了开闭原则，感觉是增加了耦合啊
#   原来的内部的判断交给用户了？？ 这不是耦合性更强了？
#   但是仔细一想，站在客户的角度出发，+-*/的操作我是知道的，所以我需要那个服务类客户应当是理解的
#   姑且就认为这适当增加的耦合性是可接受的吧


# 用工厂方法模式重写计算器类
from abc import ABC, abstractmethod


class BaseOperation(ABC):
	
	@abstractmethod
	def get_result(self, number_a, number_b):
		pass


class AddOperation(BaseOperation):
	
	def get_result(self, number_a, number_b):
		return number_a + number_b


class SubOperation(BaseOperation):
	
	def get_result(self, number_a, number_b):
		return number_a - number_b


class MulOperation(BaseOperation):
	
	def get_result(self, number_a, number_b):
		return number_a * number_b


class DivOperation(BaseOperation):
	
	def get_result(self, number_a, number_b):
		return number_a / number_b


class BaseFactory(ABC):
	
	@abstractmethod
	def create_operation(self):
		pass


class AddFactory(BaseFactory):
	
	def create_operation(self):
		return AddOperation()


class SubFactory(BaseFactory):
	
	def create_operation(self):
		return SubOperation()


class MulFactory(BaseFactory):
	
	def create_operation(self):
		return MulOperation()


class DivFactory(BaseFactory):
	
	def create_operation(self):
		return DivOperation()


# 反射可以解决分支判断的问题？？？
if __name__ == '__main__':
	number_a = int(input('please input a\n'))
	number_b = int(input('please input b\n'))
	operation = input('please input operation + | - | * | /\n')
	factory = None
	if operation == '+':
		factory = AddFactory()
	elif operation == '-':
		factory = SubFactory()
	elif operation == '*':
		factory = MulFactory()
	elif operation == '/':
		factory = DivFactory()
	op = factory.create_operation()
	print(op.get_result(number_a, number_b))
