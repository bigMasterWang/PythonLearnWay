# -*- coding: utf-8 -*- 
# @Time     : 2021/5/11 23:01 
# @Author   : wangxiaofeng01@corp.netease.com
# @desc:    : 协程

# yield item这行代码
# 1. 会产出一个值, 提供给next()的调用方
# 2. 暂停执行生成器, 让调用方继续工作, 直到需要使用另一个值时在调用next()
# 协程中 yield就是一个流程控制工具

# 本章先简单介绍生成器如何变成协程, 然后再进入核心内容
# 可能是协程最简单的使用演示
def simple_coroutine():
	print 'simple_coroutine start'
	x = yield
	print 'simple_coroutine received ', x

my_coro = simple_coroutine()
print my_coro		# <generator object simple_coroutine at 0x0000000002D7AAE8>
next(my_coro)		# simple_coroutine start
try:
	my_coro.send(12)	# simple_coroutine received  12
except StopIteration:
	print 'coroutine end'

# 启动协程使用next()和send(None)效果是一样的, 但是不能发送None之外的值
# 否则报错, TypeError: can't send non-None value to a just-started generator
# 所以一般使用next()函数, 这一步通常称为'预激'协程
my_coro_2 = simple_coroutine()
my_coro_2.send(None)
try:
	my_coro_2.send(2)
except StopIteration:
	print 'coroutine end'


# 再来一个例子
def simple_coro2(a):
	print 'start a =', a
	b = yield a
	print 'received b =', b
	c = yield a + b
	print 'received c =', c

my_coro_3 = simple_coro2(1)
# 第一个yield的return, next的时候就执行了
x = next(my_coro_3)
y = my_coro_3.send(10)
print 'x = ', x
print 'y = ', y
try:
	my_coro_3.send(300)
except StopIteration:
	print 'coroutine stop'

# 关键的一点, 协程在yield关键字所在的位置暂停执行, 前面说过, 再赋值语句中 ,
# =右边的代码在赋值之前执行, 因此, 对于 b = yield a 这行代码来说
# 等到激活(不是预激活)协程时才会设定b的值, 通俗讲就是限制性等于号右边的yield a, 返回a的值, 然后等待send给b赋值

