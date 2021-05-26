# -*- coding: utf-8 -*- 
# @Time     : 2020/8/13 14:53 
# @Author   : wangxiaofeng01@corp.netease.com
# @desc:    : 测试Serialize

class TestClass(object):
    username = None
    password = None

    def __init__(self):
        super(TestClass, self).__init__()

    @classmethod
    def GetMyClassName(self):
        print self.__class__.__name__

# 1.hasattr()
print hasattr(TestClass, 'password')
# 类在内部打印自己的classname是type
TestClass.GetMyClassName()

# 2.使用type动态生成类
dynamic = type("dynamic_class", (object,), {'role': 'dog'})
d = dynamic()
# 类直接用.__name__
print dynamic.__name__
# 实例用.__class__.__name__
print d.__class__.__name__
print d.role


# 3.使用setAttr给类动态添加属性, 但是给类添加的方法，都会默认传递一个self属性，所以添加不是类的方法，没有参数时，会提示
# TypeError: DynamicAddFunc() takes no arguments (1 given)
def DynamicAddFunc():
    print 'hello world'
setattr(dynamic, "print_my_name", DynamicAddFunc)
d.print_my_name()
