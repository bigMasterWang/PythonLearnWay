# -*- coding: utf-8 -*- 
# @Time     : 2021/5/6 20:31 
# @Author   : wangxiaofeng01@corp.netease.com
# @desc:    : 接口: 从协议到抽象基类
from abc import abstractmethod
from random import shuffle
from typing import overload

l = list(range(10))
shuffle(l)
print l

import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck(object):
	ranks = [str(n) for n in range(2, 11)] + list('JQKA')
	suits = 'spades diamonds clubs hearts'.split()

	def __init__(self):
		self._cards = [Card(rank, suit) for rank in self.ranks for suit in self.suits]

	def __len__(self):
		return len(self._cards)

	def __getitem__(self, item):
		return self._cards[item]

	def __setitem__(self, key, value):
		self._cards[key] = value


# 这个类无法被打乱
test = FrenchDeck()
print test[0]
# 报错 item assignment, 所以需要setitem
shuffle(test)
print test[0]


# 其实抽象基类的本质就是实现几个特殊的方法, 例如:
# python3 中的
# class Struggle(object):
#
# 	def __len__(self):
# 		return 23
# from collections import abc
# print isinstance(Struggle(), abc.Sized) # True

class FrenchDeck2(collections.MutableSequence):

	ranks = [str(n) for n in range(2, 11)] + list('JQKA')
	suits = 'spades diamonds clubs hearts'.split()

	def __init__(self):
		self._cards = [Card(rank, suit) for rank in self.ranks for suit in self.suits]

	def __len__(self):
		return len(self._cards)

	def __getitem__(self, item):
		return self._cards[item]

	def __setitem__(self, key, value):
		self._cards[key] = value

	# MutableSequence的抽象方法
	def __delitem__(self, i):
		del self._cards[i]

	# MutableSequence的抽象方法
	def insert(self, index, value):
		self._cards.insert(index, value)

test = FrenchDeck2()
print test[0]
shuffle(test)
print test[0]

# 标准库中的抽象基类
# 大部分都在collections.abc但是这个是python3里面的

