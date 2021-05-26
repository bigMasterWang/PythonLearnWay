# -*- coding: utf-8 -*- 
# @Time     : 2020/8/13 15:33 
# @Author   : wangxiaofeng01@corp.netease.com
# @desc:    : 得到一个py文件中所有的类

import inspect
import sys

from Serialize.TestModule.TestInner import Classes

# sys.modules[Classes.__name__] == __import__(classes.__name__)
# 方法1
current_module = sys.modules[Classes.__name__]
# print type(current_module)
# 方法2
test = __import__("Classes")


# 找出模块里所有的类名
def get_classes():
    for name, obj in inspect.getmembers(test):
        if inspect.isclass(obj):
            print name

get_classes()




# 找出模块里所有的类名
# def get_classes_two(arg):
#     for name, obj in inspect.getmembers(sys.modules[__name__], inspect.isclass):
#         print name


# import pyclbr
# print(pyclbr.readmodule(Classes.__name__).keys())