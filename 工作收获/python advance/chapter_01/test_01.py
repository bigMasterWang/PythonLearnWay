# -*- coding: utf-8 -*- 
# @Time     : 2021/4/12 12:39 
# @Author   : wangxiaofeng01@corp.netease.com
# @desc:    :


g = 9.8

class Gravity(object):

	def get(self, m):
		return m*g

obj = Gravity()
print obj.get(2)

# assinement, 全部认为是局部变量


class Foo(object):

	def __init__(self):
		self._list = [1, 2, 3, 4, 5]

	def __iter__(self):
		counter = 0
		def get():
			if counter >= len(self._list):
				return None
			res = self._list[counter]
			# 下面注释取消就会立即报错, 因为+=是一种assiment
			# counter += 1
			return res
		return iter(get, None)

a = Foo()
for item in a:
	print item

# Locating in name spaces
# From inner to outer(t009, t008)
# Write operation will shield the locating outside the current name space, which is determined at compile time(编译期)
# global statement will tell the compiler the name locating is in the global name space, not the local
# No local or upvalue statement to control the accessing of local name space
