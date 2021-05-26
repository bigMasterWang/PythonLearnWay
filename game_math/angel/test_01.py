# -*- coding: utf-8 -*- 
# @Time     : 2021/4/16 15:18 
# @Author   : wangxiaofeng01@corp.netease.com
# @desc:    : 判断两个角
import math


class Vector2(object):

	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __mul__(self, other):
		return self.x * other.x + self.y * other.y

	def __abs__(self):
		return math.hypot(self.x, self.y)


v1 = Vector2(1, 0)
v2 = Vector2(-111, 1)


# rint math.acos((v1 * v2) / (abs(v1) * abs(v2)))
print -v1.x * v2.y + v1.y * v2.x
# print math.acos((v1 * v2) / (abs(v1) * abs(v2))) <= math.pi / 2