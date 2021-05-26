# -*- coding: utf-8 -*- 
# @Time     : 2021/1/6 22:54 
# @Author   : wangxiaofeng01@corp.netease.com
# @desc:    : 第七章, 函数装饰器和闭包

"""  何时执行装饰器?"""
# 被装饰器装饰之后, 导入时就执行, 验证
my_funcs = []


def my_director(func):
	print 'running my_director'
	my_funcs.append(func)
	return func


@my_director
def f1():
	print 'running f1'


@my_director
def f2():
	print 'running f2'


@my_director
def f3():
	print 'running f3'


def main():
	print 'running main'
	print 'director: ', my_funcs
	f1()
	f2()
	f3()

main()

# 上面的有何作用呢? 比如说一等函数的策略模式, 我们使用全局属性搜索的办法来获取策略, 但是难免由名字起错的时候, 这个时候使用装饰器就再好不过了
# 写一下
# functools.wraps
