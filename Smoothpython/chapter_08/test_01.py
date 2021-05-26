# -*- coding: utf-8 -*- 
# @Time     : 2021/1/12 22:22 
# @Author   : wangxiaofeng01@corp.netease.com
# @desc:    :

"""变量不是盒子"""
# a是周树人, b是鲁迅
a = [1, 2, 3, 4]
b = a
b.append(5)
print a
print id(a), id(b)
print a is b

# ==比较对象的值, 使用的是__eq__(), is比较对象本身, 比较的可能是id() == id()


"""元组本身不可变, 元素可变"""
# 所以说, 只有元组中所有的元素都不能改变时, 才可散列
t1 = (1, 2, [3, 4])
t2 = (1, 2, [3, 4])
print t1 == t2
print id(t1), id(t1[-1])
t1[-1].append(5)
print id(t1), id(t1[-1])
print t1 == t2

"""深刻理解浅复制"""
# 复制列表最简单的方式是使用内置的类型构造方法
l1 = [3, [55, 44], (7, 8, 9)]
l2 = list(l1)
# print l2
# print l2 == l1
# print l2 is l1
# 浅复制, 直接可用[:]给列表或者其他可变序列进行浅复制
# 意思就是复制了最外层的容器, 但是副本中的元素是源容器的引用
l3 = l1[:]
# 元素的源容器是引用, 全部都会改变
l1[1].append(33)
# 复制了最外层容器, 所以添加其他的并不知道
l1.append(521)
# 因为给元组+=,直接生成了一个新的对象, 可之前的不是同一个对象了
l1[2] += (10, 11)
print l1
print l2
print l3

"""为任意对象做深浅复制"""
# copy.deepcopy()


"""不要使用可变类型作为参数的默认值"""

class Bus(object):
	"""备受幽灵折磨的校车"""

	# 注意这种写法, passengers=[], 如果使用这个[]的话, 多个实例使用的是同一个[], 是共享的
	# 那么每一次执行的时候, 都会覆盖它的默认值
	def __init__(self, passengers=[]):
		self._passengers = passengers

	def pick(self, name):
		self._passengers.append(name)

	def drop(self, name):
		self._passengers.remove(name)

	@property
	def passenagers(self):
		return self._passengers


bus1 = Bus(['alice', 'roland'])
print bus1.passenagers
bus1.drop('alice')
print bus1.passenagers

bus2 = Bus()
bus2.pick('william')
print bus2.passenagers

bus3 = Bus()
print bus3.passenagers

bus3.pick('jake')
print bus2.passenagers

# 查看一下默认值, 默认值如果是可变对象的话, 那么之后的都会可变
print Bus.__init__.__defaults__
print Bus.__init__.__defaults__[0] is bus3.passenagers
print dir(Bus.__init__)

# 8.4 防御可变参数 -------------------------------------------------------------

class TwilightBus(object):

	def __init__(self, passengers=None):
		if passengers is None:
			self.passengers = []
		else:
			self.passengers = passengers

	def pick(self, name):
		self.passengers.append(name)

	def drop(self, name):
		self.passengers.remove(name)

team_players = ['王晓峰', '张冠举']
bus = TwilightBus(team_players)
bus.drop('张冠举')
for item in team_players:
	print item

class GoodBus(object):

	def __init__(self, passengers=None):
		if passengers is None:
			self.passengers = []
		else:
			self.passengers = list(passengers)

	def drop(self, name):
		self.passengers.remove(name)
team_players = ['王晓峰', '张冠举']
bus = GoodBus(team_players)
bus.drop('张冠举')
for item in team_players:
	print item,
print


# del和垃圾回收------------------------------------
# 对象销毁时会调用__del__来给对象最后的机会进行一些操作
import weakref


class TestClass(object):

	def __init__(self):
		super(TestClass, self).__init__()

	def __del__(self):
		print 'I am gone'

s1 = TestClass()
s2 = ''

del s1
del s2
# 从上面这一段可以看出来, del s1 并没有删除对象, 而是删除的s1这个引用, 当s2也指向其他的部分时, 对象的引用为0了,才进行销毁

s1 = {1, 2}
s2 = s1
def cb(reference):
	print '{} call back'.format(reference)
wref = weakref.ref(s1, cb)
del s1
del s2


# 8.6 弱引用---------------------------------------------------------
# import weakref
# weakref(obj, cb=None)
# 返回一个引用对象, call(引用对象)的时候会返回指向的结果, 没有就返回None
a = {1, 2}
b = a
test_ref = weakref.ref(a)
print test_ref
print test_ref()
a = b = 1
print test_ref
print test_ref()

# --------------------repr and str-----------------------
# 1.	str() is used for creating output for end user while repr() is mainly used for debugging and development, repr's goal is to
# 		be unambiguous and str's is to be readable. For example, if we suspect a float has small rounding error, repr will show us while str may not
# 2.
s = 'hello world'
print str(s)
print repr(s)

import datetime
print str(datetime.datetime.now())
print repr(datetime.datetime.now())

# 一个小把戏, python用户就不用看了
# 1. 使用一个元组构建的另一个元组, 得到的其实是同一个元组
t1 = (1, 2, 3)
t2 = tuple(t1)
print t2 is t1

# 2. 字符串字面量可能会创建共享的对象
# 共享字符串字面量是一种优化措施, 称为驻留, CPython还会在小的整数上使用这个优化措施, 防止重复创建"热门"数字
t1 = (1, 2, 3)
t2 = (1, 2, 3)
print t1 is t2

s1 = 'ABC'
s2 = 'ABC'
print s1 is s2

i1 = 1
i2 = 1
print i1 is i2
# 上面这些细枝末节的最佳用途是与其他Python程序员打赌, 提高自己的胜算