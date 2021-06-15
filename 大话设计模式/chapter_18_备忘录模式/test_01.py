# -*- coding: utf-8 -*-
# @Time     : 2021/6/11 17:10
# @Author   : wangxiaofeng01@corp.netease.com
# @desc:    : 第十八章 如果再回到从前——备忘录模式


# 备忘录模式(memento): 在不破坏封装性的前提下, 捕获一个对象的内部状态,并在该对象之外保存这个状态.
# 						这样以后就可将该对象恢复到原先保存的状态

# 结构: 就是目标类写create和set memento的方法, 然后外部用一个memento类来对应状态的内容, 用一个taker类来保存这个memento
# 下面的例子, memento中就只记录了一个state的量
class Originator:

	def __init__(self):
		self.state = None

	def create_memento(self):
		return Memento(self.state)

	def set_memento(self, _memento):
		self.state = _memento.state

	def show(self):
		print('state =', self.state)


class Memento:

	def __init__(self, state):
		self.state = state


# 就是一个实例用来保存memento的
class CareTaker:

	def __init__(self):
		self.memento = None


def test_01():
	o = Originator()
	o.state = 'Good'
	o.show()

	taker = CareTaker()
	taker.memento = o.create_memento()

	o.state = 'Bad'
	o.show()

	o.set_memento(taker.memento)
	o.show()




# 使用场合:
# 功能比较复杂, 但需要维护或记录属性历史的类, 或者需要保存的属性只是众多属性中的一小部分, originator可以根据保存的memento信息还原到前一状态



class Player:

	def __init__(self, vitality, attack, defense):
		self.vitality = vitality
		self.attack = attack
		self.defense = defense

	def show(self):
		print('======================================')
		for p in self.__dict__:
			print('{}: {}'.format(p, getattr(self, p)))

	def beat_boss(self):
		print('beat boss ========================================')
		self.vitality = 5
		self.attack = 6
		self.defense = 7

	def create_memento(self):
		return PlayerMemento(self.vitality, self.attack, self.defense)

	def set_memento(self, memento):
		for p in memento.__dict__:
			setattr(self, p, getattr(memento, p))


class PlayerMemento:
	def __init__(self, vitality, attack, defense):
		self.vitality = vitality
		self.attack = attack
		self.defense = defense


class MementoTaker:

	def __init__(self):
		self.memento = None


def test_02():
	p = Player(10, 10, 10)
	p.show()
	mt = MementoTaker()
	mt.memento = p.create_memento()
	p.beat_boss()
	p.show()
	p.set_memento(mt.memento)
	p.show()


if __name__ == '__main__':
	# test_01()
	test_02()