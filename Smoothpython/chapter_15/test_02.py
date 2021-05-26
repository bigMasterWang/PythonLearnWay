# -*- coding: utf-8 -*- 
# @Time     : 2021/5/11 22:04 
# @Author   : wangxiaofeng01@corp.netease.com
# @desc:    :

import contextlib
import sys



@contextlib.contextmanager
def looking_glass():
	class A(object):
			pass
	a = A()
	for key in dir(sys.stdout):
		if key.startswith('__'):
			continue
		setattr(a, key, getattr(sys.stdout, key))
	original_print, sys.stdout = sys.stdout, a
	def reverse_write(text):
		original_print.write(text[::-1])
	a.write = reverse_write
	original_print.write('1\n')
	# 如果输出有错误, 这里要进行拦截
	try:
		yield looking_glass.__name__
	except ZeroDivisionError:
		msg = 'Please DO NOT divide by zero!'
	finally:
		sys.stdout = original_print
		if msg:
			print msg
	original_print.write('2\n')
	sys.stdout = original_print

with looking_glass() as what:
	print 1/0
print 'hello world'

# @contextlib.contextmanager 这个修饰器会把函数包装成一个
# 实现__enter__和__exit__方法的类
# 这个类的__enter__方法有如下作用
# 1. 调用生成器函数, 保存生成器对象(这里成为gen)
# 2. 调用next(gen), 执行到yield关键字所在的位置
# 3. 返回next(gen)产出的值, 以便把产出的值绑定到with/as语句中的目标变量上.
# with块终止时, __exit__方法会做以下几件事
# 1. 检查有没有异常传给exc_style, 如果有,调用gen.throw(exception), 在生成器函数定义体中
# 		包含yield关键字的那一行抛出异常
# 2. 否则, 调用next(gen), 继续执行生成器函数定义体中yield语句之后的代码

# 取出面包
# 子程序是把馅儿拿出来, 用不同的面包夹
# with是把面包拿出来, 夹不同的馅儿

# 取得原谅比获得许可容易