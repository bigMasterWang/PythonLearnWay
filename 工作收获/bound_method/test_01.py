# -*- coding: utf-8 -*- 
# @Time     : 2021/4/2 11:30 
# @Author   : wangxiaofeng01@corp.netease.com
# @desc:    : bound method

class TestClass(object):

	def __init__(self):
		super(TestClass, self).__init__()

	def test_func(self):
		print 'this is test_func'

	def get_handler(self):
		return {
			'test_func': self.test_func
		}

	def get_handler_two(self):
		return {
			'test_func': self.__class__.test_func
		}

	def get_handler_three(self):
		return {
			'test_func': TestClass.test_func
		}

a = TestClass()
print a
print a.get_handler()['test_func'].im_self
a.get_handler_two()['test_func'](a)
# print a.get_handler()['test_func'].__code__.co_varnames[0]
# print a.get_handler()['test_func'].__code__.co_cellvars
# for item in dir(a.get_handler()['test_func']):
# 	print item

# 所以上面的情况会出现闭包, self.test_func里面其实引用了self, 所以如果要解决这个问题, 可以像上面的
# get_handler_two和 get_handler_three一样
# 然后使用的时候
# get_handler_three()['test_func'](self)

