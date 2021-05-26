# -*- coding: utf-8 -*- 
# @Time     : 2021/5/9 15:44 
# @Author   : wangxiaofeng01@corp.netease.com
# @desc:    : 第十二章, 继承的优缺点

# 1. 子类化内置类型的缺点
# 2. 多重继承和方法解析顺序


# 1. 子类化内置类型的缺点
class TestDict(dict):

	def __setitem__(self, key, value):
		super(TestDict, self).__setitem__(key, [value]*2)

dd = TestDict(one=1)
print dd
dd['two'] = 2
print dd
dd.update({'three': 3})
print dd
# __init__和update忽略了__setitem__方法, self.get()不调用self.__getitem()__

class TestDictTwo(dict):

	def __getitem__(self, item):
		return 42

dd2 = TestDictTwo(a='foo')
print dd2['a']
dd = {}
# update取的也不是getitem
dd.update(dd2)
print dd['a']
print dd

# 所以直接子类化内置类型(如dict,list或者str)容易出错, 因为内置类型的方法通常会忽略用户覆盖的方法
# 所以可以使用collections.UserDict但是2中并没有

# 2. 多重继承和方法解析顺序
class A(object):

	def ping(self):
		print 'ping: ', self

class B(A):

	def pong(self):
		print 'pong:', self

class C(A):

	def pong(self):
		print 'PONG:', self

class D(B, C):

	def ping(self):
		super(D, self).ping()
		print 'PING:', self

	def pingpong(self):
		self.ping()
		super(D, self).ping()
		self.pong()
		super(D, self).pong()
		# 这样区分也可以
		C.pong(self)

d = D()
d.pingpong()
# 为了区别, 也可以这样做
print '====================================='
print C.pong(d)
# python知道调用哪个pong()是因为__mro__, 一个元组, 父类的顺序关系
print D.__mro__	# (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <type 'object'>)
print bool.__mro__

def print_mro(cls):
	print ', '.join(c.__name__ for c in cls.__mro__)

print_mro(bool)
# 方法解析顺序使用C3算法计算

