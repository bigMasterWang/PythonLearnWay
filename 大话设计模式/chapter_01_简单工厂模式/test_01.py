# coding=utf-8
# 以活字印刷举例
# 可维护(可更改),可复用,可扩展,灵活性好
# 说白了就是可变
#
#
# 计算器的领悟：
# 1. 抽象， 读取， 运算， 结果， 都要进行抽象，
#   一个读取的方法， 不管怎么读取的， 不影响计算模块进行调用
#   一个输出结果的方法， 不管怎么读取的， 不影响计算方法进行计算
#   换句话说就是抽象， 将一个系统在逻辑上抽象， 抽成几个不同的的部分
#   之间没有什么关联， 互不关心内部运算方式， 只关心输入和输出即可
#
#
# 面向对象三大特性
# 1. 封装（就是抽象，抽出来互不关联的几个类， 哎， 就是抽）
# 2. 继承，多态
# 看到几个同类别的东西就要想到将通用的东西抽取出来，然后作为基类，这里用了继承
# 然后除了通用的， 剩下的就是不通用的， 然后不同的子类写不同的方法， 这里用了多态
#
#
# 例如计算器类， 每个操作类都有一个getResult()方法， 不同的操作加减乘除都有自己的实现方式
# 这就叫继承和多态


# -*- coding: utf-8 -*-
# @Time     : 2021/5/26 21:04
# @Author   : wangxiaofeng01@corp.netease.com
# @desc:    :

def test_01():
    x = int(raw_input('please input number a\n'))
    y = int(raw_input('please input number b\n'))
    operation = raw_input('please input operation +-*/\n')
    if operation == '+':
        print x + y
    if operation == '-':
        print x - y
    if operation == '*':
        print x * y
    if operation == '/':
        print x / y


# 输入, 计算, 输出分离 封装
def test_02():
    operation, x, y = get_input()
    result = calculate_result(operation, x, y)
    print_result(result)


def calculate_result(operation, x, y):
    result = None
    if operation == '+':
        result = x + y
    if operation == '-':
        result = x - y
    if operation == '*':
        result = x * y
    if operation == '/':
        result = x / y
    return result


# 计算进行继承和多态, 继承多态和工厂模式结合
def test_03():
    import abc

    class Operation(object):

        @abc.abstractmethod
        def get_result(self, a, b):
            pass

    class AddOperation(Operation):
        def get_result(self, a, b):
            return a + b

    class SubOperation(Operation):
        def get_result(self, a, b):
            return a - b

    class MulOperation(Operation):
        def get_result(self, a, b):
            return a * b

    class DivOperation(Operation):
        def get_result(self, a, b):
            return a / b

    class OperationFactory(object):

        @staticmethod
        def getOperation(operation):
            if operation == '+':
                return AddOperation()
            if operation == '-':
                return SubOperation()
            if operation == '*':
                return MulOperation()
            if operation == '/':
                return DivOperation()

    operation, number_a, number_b = get_input()
    op = OperationFactory.getOperation(operation=operation)
    print_result(op.get_result(number_a, number_b))


def print_result(result):
    print result


def get_input():
    number_a = int(raw_input('please input number a\n'))
    number_b = int(raw_input('please input number b\n'))
    operation = raw_input('please input operation +-*/\n')
    return operation, number_a, number_b


if __name__ == '__main__':
    # test_01()
    # test_02()
    test_03()

# 上面test_01, test_02, test_03是计算器版本的演化
# 然后本章最后还讲述了uml图的用法， 这个之后在进行设计的时候，在学
# uml也不是一朝一夕能学会的， 所以之后在进行设计的时候，一定要用上uml图
