# -*- coding: utf-8 -*- 
# @Time     : 2020/8/24 17:09 
# @Author   : wangxiaofeng01@corp.netease.com
# @desc:    :

# 具名元组
from collections import namedtuple

City = namedtuple('City', 'name, country, population, coordinates')

tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))
print tokyo
print tokyo.population
print tokyo.coordinates
print tokyo[0]

# 类的所有属性
print City._fields
# 类的__dict__和实例的__dict__不一样，实例的__dict__如下
# 遍历实例的属性和值
# or item in tokyo.__dict__:

print 'ddd'
for item in tokyo.__dict__:
    print item,
    print tokyo.__getattribute__(item)

print 'eee'

for item in tokyo._fields:
    print item,
    print tokyo.__getattribute__(item)

# _make(iter)通过接收一个可迭代对象来生成一个类的实例，和 Class(*iter)作用类似
LatLong = namedtuple('LatLong', 'Lat, long')
ShangHai_data = ('ShangHai', 'CHINA', 32.000, LatLong(123, 321))
ShangHai = City._make(ShangHai_data)
# 以OrderedDict的形式返回
print ShangHai._asdict()


x = ('1', '2', '3', '4')
xx = City._make(x)
print xx._asdict()

# 我来测试一下对自己定义的类, 和上面的完全不一样，没有_filed, 没有_make()
class TestClassOne(object):

    def __init__(self, name=None, age=None, sex=None):
        super(TestClassOne, self).__init__()
        self.name = name
        self.age = age
        self.sex = sex

data = ('王晓峰', 23, '男')
test = TestClassOne(*data)
# 属性应该是实例的，类没有， namedtuple应该就是定义好了，不能改变了，所以会有类的_fileds等属性
print test.__dict__


