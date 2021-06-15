# @Time     : 2021/6/7 12:29
# @Author   : wangxiaofeng01@corp.netease.com
# @desc:    : 第16章  无尽加班何时休——状态模式

# 方法过长是坏味道: 太长就代表责任过大了, 无论改变什么都需要改变这个方法, 实际上很糟糕

# 状态模式: 当一个对象的内在状态改变时允许改变其行为, 这个对象看起来像是改变了其类
# 状态模式主要解决的是当控制一个对象状态转换的条件表达式过于复杂的情况. 把状态的判断逻辑转移到表示不同的
# 一系列类当中, 可以把复杂的判断逻辑简化.


# 结构
from abc import ABC, abstractmethod


class State(ABC):

	@abstractmethod
	def handle(self, context):
		pass


class ConcreteStateA(State):

	def handle(self, context):
		context.state = ConcreteStateA()
		print(self.__class__.__name__)


class ConcreteStateB(State):

	def handle(self, context):
		context.state = ConcreteStateB()
		print(self.__class__.__name__)


class Context:

	def __init__(self, state):
		self.state = state

	def request(self):
		self.state.handle(self)


def test_01():
	c = Context(ConcreteStateA())
	c.request()
	c.request()
	c.request()
	c.request()


# 应用场景: 当一个对象的行为取决于它的状态, 并且它必须在运行时刻根据状态改变它的行为时,就可以考虑是使用状态模式

# <12: 上午
# <13: 中午
# <17: 下午
# <21: 晚间
# >21: 睡眠工作
# : 下班


class WorkState(ABC):

	def __init__(self, _context):
		self.context = _context

	@abstractmethod
	def work(self):
		pass


class ForenoonState(WorkState):
	def work(self):
		if self.context.hour < 8:
			print('还没开始上班呢, 你着急你妈呢?')
			return
		if self.context.hour < 12:
			print('上午工作状态良好')
		else:
			self.context.state = NoonState(self.context)
			self.context.state.work()


class NoonState(WorkState):

	def work(self):
		if self.context.hour < 13:
			print('中午犯困')
		else:
			self.context.state = AfternoonState(self.context)
			self.context.state.work()


class AfternoonState(WorkState):

	def work(self):
		if self.context.hour < 17:
			print('下午工作状态良好')
		else:
			self.context.state = NightState(self.context)
			self.context.state.work()


class NightState(WorkState):
	def work(self):
		if self.context.work_finished:
			self.context.state = AfterWorkState(self.context)
			self.context.state.work()
			return
		if self.context.hour < 21:
			print('加班')
		else:
			self.context.state = SleepWorkState(self.context)
			self.context.state.work()


class AfterWorkState(WorkState):
	def work(self):
		print('下班')


class SleepWorkState(WorkState):

	def work(self):
		if self.context.work_finished:
			self.context.state = AfterWorkState(self.context)
			self.context.state.work()
			return
		print('几点了?还在加班,要睡着了')


class WorkContext:
	def __init__(self):
		self.hour = 5
		self.work_finished = False
		self.state = ForenoonState(self)

	def work(self):
		self.state.work()

def test_02():
	wc = WorkContext()
	wc.work()
	wc.hour = 7
	wc.work()
	wc.hour = 8
	wc.work()
	wc.hour = 9
	wc.work()
	wc.hour = 10
	wc.work()
	wc.hour = 11
	wc.work()
	wc.hour = 12
	wc.work()
	wc.hour = 13
	wc.work()
	wc.hour = 14
	wc.work()
	wc.hour = 15
	wc.work()
	wc.hour = 16
	wc.work()
	wc.hour = 17
	wc.work()
	wc.hour = 18
	wc.work()
	wc.hour = 19
	wc.work()
	wc.hour = 20
	wc.work()
	wc.hour = 21
	wc.work()
	wc.hour = 22
	wc.work()
	wc.hour = 23
	wc.work_finished = True
	wc.work()
	wc.hour = 24
	wc.work()



if __name__ == '__main__':
	# test_01()
	test_02()

# 总结的来讲, 就是把判断和状态的切换, 放到状态类内部,而整个状态作为用户类的一个属性