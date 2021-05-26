# -*- coding: utf-8 -*- 
# @Time     : 2021/4/27 20:28 
# @Author   : wangxiaofeng01@corp.netease.com
# @desc:    : 第十章 序列的修改, 散列和切片

# 基本的序列协议 __len__和__getitem__
# 综合哥哥元素的值计算散列值
# 自定义的格式语言扩展
# __getattr__方法实现属性的动态存取
# 穿插讨论概念: 把协议当作正式接口

# 10.3 协议和鸭子类型
import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck(object):
	ranks = [str(n) for n in range(2, 11) + list('JQKA')]
	suits = 'spades diamonds clubs hearts'.split()

	def __init__(self):
		self._cards = [Card(rank, suit) for rank in self.ranks for suit in self.suits]

	def __len__(self):
		return len(self._cards)

	def __getitem__(self, item):
		return self._cards[item]

x = FrenchDeck()


print x[0]
print len(x)
print x[1:3]


# 10.4 详解切片
class MySeq(object):

	def __getitem__(self, index):
		print index

s = MySeq()
s[1]
s[1:4]
s[1:4:2]
s[1:4:2, 9]		# (slice(1, 4, 2), 9)
s[1:4:2, 7:9]	# (slice(1, 4, 2), slice(7, 9, None))
print dir(slice)

import numbers
print isinstance(1, numbers.Integral)

# getattr和getattribute 前者是属性查找失败后调用的, 后者是属性查找

class TestClass(object):

	shorcut_names = 'xyzw'

	def __getattr__(self, item):
		cls = type(self)
		if len(item) == 1:
			pos = cls.shorcut_names.find(item)
			if 0 <= pos:
				return self.__class__.__name__, cls.shorcut_names[pos]
		print item
		self.__setattr__(item, repr(item))
		return self.item

test = TestClass()
print test.x
# 属性赋值了, 这个实例就有这个属性了,那么之后就不会走到__getattr__()里面去了
# 也可以避免这种现象 直接setattr
test.x = 10
print test.x
print test.x123

