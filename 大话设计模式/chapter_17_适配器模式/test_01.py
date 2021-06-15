
# -*- coding: utf-8 -*-
# @Time     : 2021/6/10 20:17
# @Author   : wangxiaofeng01@corp.netease.com
# @desc:    : 第17章: 在NBA我需要翻译——适配器模式

# Adapter
# 适配器模式: 将一个类的接口转换成客户希望的另外一个接口, Adapter模式使得来本由于接口不兼容而不能一起工作的那些类
# 				可以一起工作
# 如电源适配器, 电脑把电压转化为可用的电压

# 也就是系统的数据和行为都正确, 但接口不符时, 我们应该考虑使用适配器, 目的是使控制范围之外的一个原有对象与某个接口匹配
# 适配器模式主要应用于希望服用一些现存的类, 但是接口又与服用环境要求不一致的情况

# 结构如下

# 用户程序要用的类
class Target:
	def request(self):
		print('普通请求')


class Adaptee:
	def some_special_request(self):
		print('特殊请求')

# 继承Target就是为了让静态语言能够写上一句
# Target a = new Adapter()
class Adapter(Target):

	def __init__(self):
		self.adaptee = Adaptee()

	def request(self):
		self.adaptee.some_special_request()


def test_01():
	a = Adapter()
	a.request()


# 一般境况下都是因为开发人员流动, 新人要兼容老人的代码, 搞这种模式
# 但也有一开始就计划使用适配器模式的情况, 如考虑使用第三方开发组件, 但是接口与自己的系统是不相同的

from abc import ABC, abstractmethod

class Player(ABC):

	def __init__(self, name):
		self.name = name

	@abstractmethod
	def attack(self):
		pass

	@abstractmethod
	def defense(self):
		pass


class Forwards(Player):
	def attack(self):
		print('forward {} attack'.format(self.name))

	def defense(self):
		print('forward {} defense'.format(self.name))

class Center(Player):
	def attack(self):
		print('center {} attack'.format(self.name))

	def defense(self):
		print('center {} defense'.format(self.name))

class Guards(Player):
	def attack(self):
		print('guards {} attack'.format(self.name))

	def defense(self):
		print('guards {} defense'.format(self.name))

# 这个类本来就要与其他的不同, 因为这个类是外来的, 接口名称不一样, 但是功能还是差不多的
# adapter就要修饰它去适配主要的环境
class ChineseCenter:

	def __init__(self, name):
		self.name = name

	def gogogo(self):
		print('中锋'+self.name+'进攻')

	def back(self):
		print('中锋'+self.name+'防守')

class Translator(Player):

	def __init__(self, name):
		self.adaptee = ChineseCenter(name)

	def attack(self):
		print('进攻翻译')
		self.adaptee.gogogo()

	def defense(self):
		print('防守翻译')
		self.adaptee.back()


def test_02():
	f = Forwards('player_one')
	c = Center('player_two')
	g = Guards('player_three')
	cp = Translator('姚明')
	f.attack()
	f.defense()
	c.attack()
	c.defense()
	g.attack()
	g.defense()
	cp.attack()
	cp.defense()


if __name__ == '__main__':
	# test_01()
	test_02()