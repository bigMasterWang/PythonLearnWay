# -*- coding: utf-8 -*- 
# @Time     : 2020/8/13 16:41 
# @Author   : wangxiaofeng01@corp.netease.com
# @desc:    : 根据文件路径，得到module

import imp
# foo = imp.load_module(name='Classes', file="../Serialize/TestModule/Classes.py", filename='Classes')
# 斜杠和反斜杠都无所谓
foo = imp.load_source('ClassesTwo', '../Serialize/ClassesTwo.py')
foo2 = imp.load_source('result', '../Serialize/result.py')


print foo
print type(foo)

# print foo2
# print type(foo2)



# 1、得到给出的文件夹中所有文件的路径
# 2、根据这些路径，得到module数组
# 3、得到这些modules中的类以及类名