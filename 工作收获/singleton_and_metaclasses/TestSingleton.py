# -*- coding: utf-8 -*- 
# @Time     : 2021/4/8 22:24 
# @Author   : wangxiaofeng01@corp.netease.com
# @desc:    : 看看这个singleton到底是怎么回事儿

class Singleton(type):

	# type的__call__(), 会调用__init__()
	def __call__(cls, *args, **kwargs):
		if not hasattr(cls, '_instance'):
			cls._instance = super(Singleton, cls).__call__(*args, **kwargs)
		return cls._instance


class PhysicsController(object):
	__metaclass__ = Singleton

	def __init__(self):
		pass

	# def __new__(cls, *args, **kwargs):
	# 	cls.__init__()


physics_controller = PhysicsController()


