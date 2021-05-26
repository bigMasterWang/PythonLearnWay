# -*- coding: utf-8 -*- 
# @Time     : 2021/4/8 22:36 
# @Author   : wangxiaofeng01@corp.netease.com
# @desc:    : metaclasses学习

"""1. type 是什么?"""
# type in Python enables us to find the type of an object. We can proceed to check the type of object we created above.


class TestClass(object):
	pass


print type(TestClass)
print type(type)
# <type 'type'>
# <type 'type'>

# 1. We'd expect the type of the object we created above to be class, but it's not.
# 2.  We also notice that the type of type itself is type. It is an instance of type.
# 3. Another magical thing that type does is enable us to create classes dynamically.


class DataCamp(object):
	pass

DataCampClass = type('DataCamp', (), {})
print DataCampClass
print DataCamp
# <class '__main__.DataCamp'>
# <class '__main__.DataCamp'>

# 1. DataCampClass is the variable that holds the class reference.
