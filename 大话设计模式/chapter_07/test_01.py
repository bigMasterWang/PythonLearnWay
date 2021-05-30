# coding=utf-8
# 为别人做嫁衣----代理模式


# 代理模式: 为其他对象提供一种代理以控制对这个对象的访问

from abc import ABC, abstractmethod

"""下面来看看代理模式的结构"""


# 目标类和代理类共同的父类， 用来定义接口用
class SubClass(ABC):
	
	def __init__(self):
		super().__init__()
	
	@abstractmethod
	def give_gifts(self):
		pass


# 目标类，一个真实的追求者
class Pursuer(SubClass):
	
	def give_gifts(self):
		print('i am real pursuer')


# 代理类，代理追求者送东西的人
class Proxy(SubClass):
	
	def __init__(self):
		super().__init__()
		self._pursuer = Pursuer()
	
	def give_gifts(self):
		print('i am proxy')
		self._pursuer.give_gifts()


if __name__ == '__main__':
	proxy = Proxy()
	proxy.give_gifts()

# 代理模式其实就是访问对象时引入一定的间接性，因为这种间接性可以附加多种用途
# 1. 远程代理：本地没这个类， 这个类会请求网络消息，并将结果返回给这个类， 客户看来就根本地使用一样
# 2. 虚拟代理：作为创建开销大的类的代码， 在这个对象创建前和创建中代理这个类， 比如html网页的图片
# 3. 安全代理：给对象加上访问权限
# 4. 智能指引：当调用真实对象时，代理去做另外的一些事情，比如计算对象的引用次数等等
