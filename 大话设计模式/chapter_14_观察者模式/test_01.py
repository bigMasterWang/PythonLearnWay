# 第十四章 老板回来,我不知道——观察者模式

# 观察者模式(又叫发布-订阅模式): 定义了一种一对多的依赖关系, 让多个观察者对象同时监听某一个主题对象
# 这个主题对象在状态发生变化时,会通知所有观察者对象,使他们能够自动更新自己

# 看一下观察者模式的结构
from abc import ABC, abstractmethod


# 主题类
class Game:

	def __init__(self):
		self.observers = []

	def attach(self, ob):
		self.observers.append(ob)

	def detach(self, ob):
		self.observers.remove(ob)

	def notify(self):
		for ob in self.observers:
			ob.update()


class GTA5(Game):

	def __init__(self):
		super().__init__()
		self._state = None

	@property
	def state(self):
		return self._state

	@state.setter
	def state(self, value):
		self._state = value


# 其实应该用抽象接口, 因为实际的生产中, 观察者可能是风马牛不相及的类
class Observer(ABC):

	@abstractmethod
	def update(self):
		pass


# !!!!!!!!!!!!!!!!!!具体观察者可以保存一个指向具体主题对象的引用
class ConcreteObserver(Observer):

	def __init__(self, name, game):
		self.name = name
		self.game = game

	def update(self):
		print('观察者 {} 被游戏 {} 通知 {}'.format(self.name, self.game.__class__.__name__, self.game.state))


if __name__ == '__main__':
	gta = GTA5()
	ob_1 = ConcreteObserver('龙斌', gta)
	ob_2 = ConcreteObserver('王晓峰', gta)
	gta.attach(ob_1)
	gta.attach(ob_2)
	gta.state = 'gta5大更新'
	gta.notify()


# 观察者使用情况:
#	当一个对象的改变需要同时改变其他对象的时候, 而且他不知道具体多少对象有待改变, 应该考虑使用观察者模式

# 观察者模式所做的工作就是在解除耦合, 让耦合双方都依赖于抽象,而不是依赖于具体. 从而使各自的变化都不会影响另一边的变化

# 观察者的不足
# 1. 观察者和被观察者还是相互引用, 互相知道的
# 2. 观察者不一定非要是update方法, 两个观察者用不同的update方法不行吗???

"""test_02用python实现delegate的流程,顺便实现事件注册"""

