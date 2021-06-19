# 第二十四章 加薪非要老总批?——职责链模式


# 职责链模式： 使多个对象都有机会处理请求，从而避免请求的发送者和接收者之间的耦合关系。 将这个对象连城一条链
#               并沿着这条链传递该求情，直到有一个对象处理它为止

from abc import ABC, abstractmethod


class AbstractProcessor(ABC):
	
	def __init__(self):
		self.superior = None
	
	def set_my_superior(self, _processor):
		self.superior = _processor
	
	@abstractmethod
	def handle(self, request):
		pass


class ProcessorOne(AbstractProcessor):
	
	def handle(self, request):
		if request <= 10:
			print('processor: {} handle request: {}'.format(self.__class__.__name__, request))
		else:
			self.superior.handle(request)


class ProcessorTwo(AbstractProcessor):
	def handle(self, request):
		if request <= 20:
			print('processor: {} handle request: {}'.format(self.__class__.__name__, request))
		else:
			self.superior.handle(request)


class ProcessorThree(AbstractProcessor):
	def handle(self, request):
		if request <= 30:
			print('processor: {} handle request: {}'.format(self.__class__.__name__, request))
		else:
			self.superior.handle(request)


def test_01():
	requests = [2, 7, 12, 16, 22, 25]
	processor_one = ProcessorOne()
	processor_two = ProcessorTwo()
	processor_three = ProcessorThree()
	processor_one.set_my_superior(processor_two)
	processor_two.set_my_superior(processor_three)
	
	for request in requests:
		processor_one.handle(request)


# 加薪代码：
class Request:
	RAISE_TYPE = '加薪'
	LEAVE_TYPE = '请假'
	
	def __init__(self, _type, _count):
		self.type = _type
		self.count = _count
	
	def __repr__(self):
		return '请求类别：{} 数量：{}'.format(self.type, str(self.count))


class Manager(ABC):
	
	def __init__(self):
		self.superior = None
	
	def set_superior(self, manager):
		self.superior = manager
	
	@abstractmethod
	def handle(self, request):
		pass
	
	def accept(self, request):
		print('manager: {} 批准请求：{}'.format(self.__class__.__name__, repr(request)))
	
	def refuse(self, request):
		print('manager: {} 拒绝请求：{}'.format(self.__class__.__name__, repr(request)))


class MyLeader(Manager):
	
	def handle(self, request):
		if request.type == Request.LEAVE_TYPE and request.count <= 2:
			self.accept(request)
		else:
			self.superior.handle(request)


class GroupLeader(Manager):
	
	def handle(self, request):
		if request.type == Request.LEAVE_TYPE and request.count <= 5:
			self.accept(request)
		else:
			self.superior.handle(request)


class Producer(Manager):
	
	def handle(self, request):
		if request.type == Request.LEAVE_TYPE and request.count <= 7:
			self.accept(request)
		elif request.type == Request.LEAVE_TYPE and request.count <= 10:
			self.refuse(request)
		elif request.type == Request.RAISE_TYPE and request.count <= 1000:
			self.accept(request)
		else:
			self.refuse(request)


def test_02():
	my_leader = MyLeader()
	group_leader = GroupLeader()
	producer = Producer()
	my_leader.set_superior(group_leader)
	group_leader.set_superior(producer)
	
	requests = [
		Request(Request.LEAVE_TYPE, 1),
		Request(Request.LEAVE_TYPE, 4),
		Request(Request.LEAVE_TYPE, 6),
		Request(Request.LEAVE_TYPE, 8),
		Request(Request.RAISE_TYPE, 1000),
		Request(Request.RAISE_TYPE, 2000),
	]
	
	for request in requests:
		my_leader.handle(request)


if __name__ == '__main__':
	# test_01()
	test_02()
