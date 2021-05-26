# -*- coding: utf-8 -*- 
# @Time     : 2021/5/18 20:14 
# @Author   : wangxiaofeng01@corp.netease.com
# @desc:    : 元编程部分, 第十九章 动态属性和特性

# __setattr__, __getattr__

import keyword


class FrozenJSON(object):

	def __init__(self, mapping):
		self.__data = dict(mapping)

	def __getattr__(self, item):
		# 这个if没有, 也没什么差别
		if hasattr(self.__data, item):
			return getattr(self.__data, item)
		else:
			return FrozenJSON.build(self.__data[item])

	@classmethod
	def build(cls, obj):
		if isinstance(obj, dict):
			return cls(obj)
		else:
			return obj


x = FrozenJSON({'a': {'b': 1}})
print x.a.b

# 但是上面的没有对python的关键字进行处理
grad = FrozenJSON({'name': 'Tom', 'class': 1982})


# print grad.class # SyntaxError: invalid syntax

# 兼容keyword的类
class KeyWordJson(FrozenJSON):

	def __init__(self, mapping):
		self.__data = {}
		for key, value in mapping.iteritems():
			if keyword.iskeyword(key):
				key += '_'
			self.__data[key] = value

	def __getattr__(self, item):
		# 这个if没有, 也没什么差别
		if hasattr(self.__data, item):
			return getattr(self.__data, item)
		else:
			return KeyWordJson.build(self.__data[item])

grad_2 = KeyWordJson({'name': 'Tom', 'class': 1982})
print grad_2.class_
