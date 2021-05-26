# -*- coding: utf-8 -*- 
# @Time     : 2021/5/25 20:27 
# @Author   : wangxiaofeng01@corp.netease.com
# @desc:    :

from evalsupport import deco_alpha
from evalsupport import MetaAleph

print '<[{}]> evaltime module start'.format(1)


class ClassOne(object):
	print '<[{}]> ClassOne body'.format(2)

	def __init__(self):
		print '<[{}]> ClassOne __init__'.format(3)

	def __del__(self):
		print '<[{}]> ClassOne __del__'.format(4)

	def method_x(self):
		print '<[{}]> ClassOne method_x'.format(5)

	class ClassTwo(object):
		print '<[{}]> ClassTwo body'.format(6)

@deco_alpha
class ClassThree(object):
	print '<[{}]> ClassThree body'.format(7)

	def method_y(self):
		print '<[{}]> ClassThree method_y'.format(8)


class ClassFour(object):
	print '<[{}]> ClassFour body'.format(9)

	def method_y(self):
		print '<[{}]> ClassFour method_y'.format(10)

class ClassFive(object):

	# 这个'类'创建时就会调用
	__metaclass__ = Meta4Aleph

	print '<[{}]> ClassFive body'.format(11)

	def __init__(self):
		print '<[{}]> ClassFive __init__'.format(12)

	def method_z(self):
		print '<[{}]> ClassFive method_z'.format(13)

class ClassSix(ClassFive):
	print '<[{}]> ClassSix body'.format(14)

	def method_z(self):
		print '<[{}]> ClassSix method_z'.format(15)


if __name__ == '__main__':
	print '<[16]> ClassOne Test', '*' * 30
	one = ClassOne()
	one.method_x()
	print '<[17]> ClassThree Test', '*' * 30
	three = ClassThree()
	three.method_y()
	print '<[18]> ClassFour Test', '*' * 30
	four = ClassFour()
	four.method_y()
	print '<[19]> ClassFive Test', '*' * 30
	five = ClassFive()
	five.method_z()
	print '<[20]> ClassFive Test', '*' * 30
	six = ClassSix()
	six.method_z()
	print '<[21]> evaltime module end'

