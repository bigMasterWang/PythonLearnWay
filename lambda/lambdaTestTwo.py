# -*- coding: utf-8 -*- 
# @Time     : 2020/8/16 15:20 
# @Author   : wangxiaofeng01@corp.netease.com
# @desc:    :

# Syntax

# 1. it can only contain expressions and can't include statements in its body
#       [ print (lambda x: assert / return  x == 2 )(2) ]
# 2. it is written as a single line of execution
        # 在python中，判断的结果返回的是最后一个判断项的值
        # print (lambda x: ('even' if x % 2 == 0 else 'odd'))(3)
# 3. it does not support type annotations
#         def test(first):
#             """
#             :rtype: int
#             :type first: int
#             """
#             return first
#
#         a = ""  # type: str
#         a = test(1)
# 4. it can be immediately invoked



# Arguments
# Like a normal function object defined with def,
# Python lambda expressions support all the different ways of passing arguments. This includes:

# Positional arguments
print ( lambda x, y ,z: x + y + z)(1, 2, 3)
# Named arguments (sometimes called keyword arguments)
print ( lambda x, y, z=3: x + y + z)(1, 2)
# Variable list of arguments (often referred to as varargs)
print ( lambda x, y=1, z=3: x + y + z)(1, y=2)
# Variable list of keyword arguments
print ( lambda *args: sum(args) )(1, 2, 3)
# Keyword-only arguments
print ( lambda **kwargs: sum(kwargs.values()))(a=1, b=2, c=3)


# 然后鞋面就写了一大堆lambda可以用到的地方，用来用去，也都是为了说明，凡是function可以用的，lambda都可以用
# 比如decorator的修饰器，closure等
# 一个比较有意思的例子：
numbers = 'one', 'two', 'three'
funcs = []
for n in numbers:
    funcs.append(lambda n=n: n)
for f in funcs:
    print f()


# lambda expression abuses
# 接下来就是仁者见仁，智者见智了
# If you find yourself trying to overcome something that a lambda expression does not support,
# this is probably a sign that a normal function would be better suited.
# It doesn’t follow the Python style guide (PEP 8)
# It’s cumbersome and difficult to read.
# It’s unnecessarily clever at the cost of difficult readability.
