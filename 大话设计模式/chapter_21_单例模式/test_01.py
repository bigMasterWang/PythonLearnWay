# -*- coding: utf-8 -*-
# @Time     : 2021/6/16 20:47
# @Author   : wangxiaofeng01@corp.netease.com
# @desc:    : 第二十章 有些类也需计划生育——单例模式

# 单例模式: 保证一个类仅有一个实例,并提供一个访问它的全局访问点

# 结构

class MySingleton:
	def __init__(self):
		pass

	_instance = None

	@classmethod
	def get_instance(cls):
		if cls._instance is None:
			cls._instance = MySingleton()
		return cls._instance


def test_01():
	x = MySingleton.get_instance()
	y = MySingleton.get_instance()
	print(x is y)


"""python的单例模式的几种实现方法"""


# 1. decorator
def singleton_decorator(_class):
	instance = {}

	def get_instance(*args, **kwargs):
		if _class not in instance:
			instance[_class] = _class(*args, **kwargs)
		return instance[_class]

	return get_instance


@singleton_decorator
class PythonSingletonOne:
	pass


def test_02():
	x = PythonSingletonOne()
	y = PythonSingletonOne()
	print(x is y)


# 2. base class
class PythonSingletonTwo:
	_instance = None

	def __new__(cls, *args, **kwargs):
		if not isinstance(cls._instance, cls):
			cls._instance = object.__new__(cls, *args, **kwargs)
		return cls._instance


class PythonSingletonTwoChildren(PythonSingletonTwo):
	pass


def test_03():
	x = PythonSingletonTwoChildren()
	y = PythonSingletonTwoChildren()
	print(x is y)


# 3. metaclass
class PythonSingletonThree(type):
	def __call__(cls, *args, **kwargs):
		if not hasattr(cls, '_instance'):
			cls._instance = super(PythonSingletonThree, cls).__call__(*args, **kwargs)
		return cls._instance


class MyClass(metaclass=PythonSingletonThree):
	pass


def test_04():
	x = MyClass()
	y = MyClass()
	print(x is y)


if __name__ == '__main__':
	test_01()
	test_02()
	test_03()
	test_04()


# 多线程单例的双重枷锁网上浏览一下即可