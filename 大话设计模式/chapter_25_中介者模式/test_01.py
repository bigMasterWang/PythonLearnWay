# 第二十五章 世界需要和平——中介者模式


# 中介者模式: 用一个中介对象来封装一系列的对象交互. 中介者使各对象不需要显式的交互,从而使其耦合松散,而且可以独立的改变他们之间的交互

from abc import ABC, abstractmethod


class Colleague(ABC):
	
	def __init__(self, mediator):
		self.mediator = mediator
	
	@abstractmethod
	def notify(self, message):
		"""

		:type message: str
		"""


class Mediator(ABC):
	
	@abstractmethod
	def send(self, message, colleague):
		"""

		:type colleague: Colleague
		:type message: str
		"""


class ConcreteMediator(Mediator):
	
	def __init__(self):
		self.colleague_one = None
		self.colleague_two = None
	
	def set_one(self, _colleague):
		self.colleague_one = _colleague
	
	def set_two(self, _colleague):
		self.colleague_two = _colleague
	
	def send(self, message, colleague):
		if colleague == self.colleague_one:
			self.colleague_two.notify(message)
		if colleague == self.colleague_two:
			self.colleague_one.notify(message)


class ConcreteColleagueOne(Colleague):
	
	def __init__(self, mediator):
		self.mediator = mediator
	
	def send(self, message):
		print('同事:{} 发送消息: {}'.format(self.__class__.__name__, message))
		self.mediator.send(message, self)
	
	def notify(self, message):
		print('同事:{} 收到消息: {}'.format(self.__class__.__name__, message))


class ConcreteColleagueTwo(Colleague):
	
	def __init__(self, mediator):
		self.mediator = mediator
	
	def send(self, message):
		print('同事:{} 发送消息: {}'.format(self.__class__.__name__, message))
		self.mediator.send(message, self)
	
	def notify(self, message):
		print('同事:{} 收到消息: {}'.format(self.__class__.__name__, message))


def test_01():
	m = ConcreteMediator()
	c1 = ConcreteColleagueOne(m)
	c2 = ConcreteColleagueTwo(m)
	
	m.set_one(c1)
	m.set_two(c2)
	
	c1.send('你吃了饭了吗?')
	c2.send('没呢, 现在去吧')

# 中介者模式一般应用于一组对象以定义良好但是复杂的方式进行通信的场合, 以及想定制一个分布在多个类中的行为, 而又不想生成太多子类的场合

# 联合国安全理事会, 美国, 阿富汗

class UniteNation(ABC):
	
	@abstractmethod
	def declare(self, country, message):
		pass


class Country(ABC):
	def __init__(self, unite_nation):
		self.unite_nation = unite_nation
	
	@abstractmethod
	def declare(self, message):
		pass
	
	@abstractmethod
	def get_message(self, message):
		pass


class America(Country):
	
	def declare(self, message):
		print('美国发布消息: {}'.format(message))
		self.unite_nation.declare(self, message)
	
	def get_message(self, message):
		print('美国收到消息: {}'.format(message))


class Iraq(Country):
	
	def declare(self, message):
		print('伊拉克发布消息: {}'.format(message))
		self.unite_nation.declare(self, message)
	
	def get_message(self, message):
		print('伊拉克收到消息: {}'.format(message))


class UniteNationSecurityCouncil(UniteNation):
	def __init__(self):
		self.countries = set()
	
	def add_country(self, country):
		self.countries.add(country)
	
	def declare(self, country, message):
		for c in self.countries:
			if c != country:
				c.get_message(message)


def test_02():
	unsc = UniteNationSecurityCouncil()
	america = America(unsc)
	iraq = Iraq(unsc)
	
	unsc.add_country(america)
	unsc.add_country(iraq)
	
	america.declare('萨达姆, 你独裁, 你有恐怖主义倾向, 我要干死你')
	iraq.declare('恐怕不是如此吧, 你就是为了石油, 真TM废物一个, 恶心的资本主义, 吃人的资本主义')
	



if __name__ == '__main__':
	test_01()
	test_02()
