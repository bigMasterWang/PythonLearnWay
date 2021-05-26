# -*- coding: utf-8 -*- 
# @Time     : 2021/5/10 22:07 
# @Author   : wangxiaofeng01@corp.netease.com
# @desc:    : 上下文管理器和else块

# enter() 返回一个对象, 然后with xxx as something, 用来赋值给后面的something

import sys


class LookingGlass(object):

	def __init__(self):
		self.original_print = None

	def __enter__(self):
		class A(object):
			pass
		a = A()
		for key in dir(sys.stdout):
			if key.startswith('__'):
				continue
			setattr(a, key, getattr(sys.stdout, key))
		self.original_print, sys.stdout = sys.stdout, a
		a.write = self.reverse_write
		return LookingGlass.__class__.__name__

	def reverse_write(self, text):
		self.original_print.write(text[::-1])

	# exc_type: 异常类
	# exc_val: 异常实例
	# traceback: traceback对象
	def __exit__(self, exc_type, exc_val, exc_tb):
		import sys
		print '__exit__'
		sys.stdout = self.original_print
		print '__exit__'
		if exc_type is ZeroDivisionError:
			print 'Please DO NOT divide by zero!'
			return True


with LookingGlass() as what:
	print 'this is a sentence'
	print what

manager = LookingGlass()
monster = manager.__enter__()
print monster == LookingGlass.__class__.__name__
manager.__exit__(None, None, None)
print monster == LookingGlass.__class__.__name__

# import sys
# class MyPrint(object):
# 	pass
#
# my_print = MyPrint()
#
# for key in dir(sys.stdout):
# 	if key.startswith('__'):
# 		continue
# 	setattr(my_print, key, getattr(sys.stdout, key))
#
# original_print, sys.stdout = sys.stdout, my_print
#
# def new_print(text):
# 	if text == '\n':
# 		original_print.write('\n')
# 		return
# 	original_print.write('hello '+text)
#
# my_print.write = new_print
# print 'world'
# print 'world'

