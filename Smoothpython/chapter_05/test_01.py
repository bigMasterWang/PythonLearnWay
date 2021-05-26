# -*- coding: utf-8 -*- 
# @Time     : 2020/9/2 16:37 
# @Author   : wangxiaofeng01@corp.netease.com
# @desc:    : 第三部分 把函数视作对象, 第五章 一等函数
# 虽然我把函数定为一等对象,但是我并不把python当作函数式编程语言
# 在python中函数就是一等对象

"""一等对象"""


# 1.能在运行时创建
# 2.能赋值给变量或数据结构中的元素
# 3.能作为参数传递给函数
# 4.能作为函数的返回结果


def test_func(args=None):
    """这里是doc文档"""
    print 'hello world'
    return args * (-1)


print test_func.__doc__
print type(test_func)

"""展示一等特性"""
test = test_func
print test
test()
print map(test, range(10))
# map( function(param), iterable) -> return iterable
# 有了一等函数,就可以使用函数式编程风格.函数式编程的特点之一就是
# 使用高阶函数

"""高阶函数"""
# 接受函数作为参数, 或者把函数作为结果返回的函数就是高阶函数
# 如map,sorted,
fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']
# 任何单参数的函数都能作为key
print sorted(fruits, key=len)


def reverse(word):
    return word[::-1]


print reverse('testing')
print sorted(fruits)
print sorted(fruits, key=reverse)

# 在高阶函数中最为人熟知的有map, filter, reduce
# 但是有了列表推导和生成器表达式,map和filter就没那么重要了
# all和any,全部/只要有 真值,返回True, false
print all(range(1, 10))
print any(range(0, 1, 1))

"""匿名函数"""
# 就是lambda, 除了作为参数给高阶函数传递参数外, python很少使用匿名函数
print sorted(fruits, key=lambda x: x[::-1])

"""可调用对象"""
print callable(test_func)
print callable(fruits)

"""用户定义的可调用类型"""


# 只要写__call__()函数就行
class ZhangLi(object):

    def __init__(self):
        self.word = '我是张力,昵称是力霸王'

    def __call__(self, *args, **kwargs):
        print args[0], kwargs.values()[0], self.word


a = ZhangLi()

print a('你好啊', response='我很好傻逼')

"""函数内省"""
print dir(test_func)


# 打印出来的都是test_func的属性,其中大多数是python对象共有的

# 列出函数有 而常规对象没有的属性
class TestClass(object):
    pass


def TestFunc():
    pass


print set(dir(TestFunc)) - set(dir(TestClass))

"""从定位参数到仅限关键词参数"""


# 主要的就是说,**attrs作为参数,本来用来接收全部的字典参数

def tag(name, cls=None, *content, **attrs):
    pass


# """偶尔之学"""
# class TestClass(object):
#
#     def __init__(self):
#         super(TestClass, self).__init__()
#
#     def __getattr__(self, item):
#
#         def call(self, *args, **kwargs):
#             info = {
#                 'called_name': item,
#                 'args': args
#             }
#             print info
#         setattr(TestClass, item, call)
#         return getattr(self, item)
#
#
# a = TestClass()
# a.cnmd('hello world')


"""获取关于参数的信息"""


def func_test(name, age=1, cnmd = 2):
    """这是函数签名"""
    print name, age


# 参数数量
print func_test.__code__.co_argcount
# 参数名称
print func_test.__code__.co_varnames
import inspect

print inspect.getargspec(func_test)

