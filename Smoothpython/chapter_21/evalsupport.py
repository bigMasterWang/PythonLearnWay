# -*- coding: utf-8 -*- 
# @Time     : 2021/5/25 20:39 
# @Author   : wangxiaofeng01@corp.netease.com
# @desc:    :

print '<[{}]> evalsupport module start'.format(100)


# 修饰器本身在顶层被import的时候并不会被执行
# 但是在别的文件顶层做修饰的时候, 就会执行
# 但是被修饰的限制性定义体, 在执行这个修饰器
def deco_alpha(cls):
	print '<[{}]> deco_alpha'.format(200)

	def inner_1(self):
		print '<[{}]> deco_alpha:inner_1'.format(300)

	cls.method_y = inner_1
	return cls


class MetaAleph(type):
	print '<[{}]> MetaAleph body'.format(400)

	def __init__(cls, name, bases, dic):
		print '<[{}]> MetaAleph __init__'.format(500)

		def inner_2(self):
			print '<[{}]> MetaAleph inner_2'.format(600)
		cls.method_z = inner_2

print '<[{}]> evalsupport module end'.format(700)
