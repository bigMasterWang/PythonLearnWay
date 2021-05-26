# -*- coding: utf-8 -*- 
# @Time     : 2020/8/19 14:48 
# @Author   : wangxiaofeng01@corp.netease.com
# @desc:    : 更加深入的使用：


class Vector(object):

    def __init__(self, x=0, y=0):
        super(Vector, self).__init__()
        self.x = x
        self.y = y

    # +运算符重载
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    # 乘运算符重载
    def __mul__(self, other):
        return Vector(self.x * other.x, self.y * other.y)

    # abs的调用
    def __abs__(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    # 减运算符重载
    def __sub__(self, other):
        pass

    # 除运算符重载
    def __div__(self, other):
        pass

    # 字符串表示形式
    # str() 和 print 调用  __str__
    def __str__(self):
        return 'Vector({0}, {1})'.format(self.x, self.y)

    # python 需要调用__str__()而没有的时候，会调用__repr__()
    def __repr__(self):
        return 'Vector({0}, {1})'.format(self.x, self.y)


a = Vector(3, 4)
b = Vector(3, 4)
print abs(a + b)
print type(a + b)
print a + b
print str(a + b)

test_one = [1, 2, 3, 4, 5, 6, 1, 2, 3]
# 计算一个value在list中出现了多少次
print test_one.count(1)

# 为什么len不是普通方法？为了效率，为了实用，实用胜于纯粹

# 总结下来就是
# 1、 通过实现特殊方法，自定义数据类型可以表现的跟内置类型一样，从而写出更具有表达力的代码，或者说更具有风格的代码
