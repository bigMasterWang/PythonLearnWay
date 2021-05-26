# -*- coding: utf-8 -*-
# @Time     : 2020/9/13 14:32 
# @Author   : wangxiaofeng01@corp.netease.com
# @desc:    :

"""5.10 支持函数式编程的包"""
"""5.10.1 operator模块"""
from functools import reduce
def fact(n):
    # reduce高阶函数,根据传入的第一个两参函数,和第二个iterable,返回一个数据
    return reduce(lambda a, b: a*b, range(1, n+1))

print fact(5)
from operator import mul
# 不能直接reduce(sum, rang(1,6)) 因为sum(iterable)不是sum(a, b)
print reduce(mul, range(1, 6))

metro_data = [
    ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
    ('Delhi', 'JP', 36.933, (35.689722, 139.691667)),
    ('Mexico City', 'JP', 36.933, (35.689722, 139.691667)),
    ('New York-Newark', 'JP', 36.933, (35.689722, 139.691667)),
    ('Sao Paulo', 'JP', 36.933, (35.689722, 139.691667))
]
# print sorted(metro_data, key=lambda x: x[0])
# 下面这种可有可无了,多次一举,还是挺牛逼的,支持'.'的嵌套和字典参数
from operator import itemgetter
# print sorted(metro_data, key=itemgetter(0))

# for item in metro_data:
#     print (lambda x: (x[0], x[1]))(item)
cc_name = itemgetter(0, 1)
# 两者效果一样
for item in metro_data:
    print cc_name(item)
# 我们手动简单的实现以下 itemgetter
def MyGetItem(*args):
    def inner(array):
        result = [array[item_index] for item_index in args]
        return tuple(result)
        # 这样使用的是generator, 需要使用.next(),并不是tuple
        # return (array[item_index] for item_index in args)
    return inner

my_name = MyGetItem(0, 1)
for item in metro_data:
    print my_name(item)

print sorted(metro_data, key=MyGetItem(0))

# 再深入一些使用 attrgetter使用的是对象的属性而已
from collections import namedtuple
LatLong = namedtuple('LatLong', 'Lat Long')
Metropolis = namedtuple('Metropolis', 'name, cc, pop, coord')
metro_areas = [Metropolis(name, cc, pop, LatLong(lat, long)) for
               name, cc, pop, (lat, long) in metro_data]

print metro_areas
from operator import attrgetter
test_attr = attrgetter('coord.Lat')
for item in metro_areas:
    print test_attr(item)

# 打印operator中的函数部分,'_'开头的基本上是实现的细节
import operator
print [name for name in dir(operator) if not name.startswith('_')]

# 更傻逼的用法
s = 'the time has come'
upcase = operator.methodcaller('upper')
print upcase(s)
repalcecase = operator.methodcaller('replace', ' ', '-')
print repalcecase(s)


"""5.10.2 使用functools.partial冻结参数"""
"""脱了裤子放屁,还好python2中并没有如此傻逼的东西"""
print map(lambda x: x*3, range(1, 10))

triple = operator.partial(mul, 3)
print map(triple, range(1, 10))