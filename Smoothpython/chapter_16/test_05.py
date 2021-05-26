# -*- coding: utf-8 -*- 
# @Time     : 2021/5/12 20:40 
# @Author   : wangxiaofeng01@corp.netease.com
# @desc:    : yield from

def gen():
	for c in 'AB':
		yield c
	for i in range(1, 3):
		yield i

print list(gen())

# python 3.3之前也不能使用yield from 'AB'
# def gen2():
# 	yield from 'AB'

