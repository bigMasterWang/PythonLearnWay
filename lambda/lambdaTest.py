# -*- coding: utf-8 -*- 
# @Time     : 2020/8/16 14:00 
# @Author   : wangxiaofeng01@corp.netease.com
# @desc:    : all examples are tested in python 2.7

# how python lambda came to be
# how lambdas compare with regular function objects
# how to write lambda functions
# which functions in the python standard libaray leverage lambdas
# when to use or avoid python lambda functions

# first Example

def identity(x):
    return x


a = lambda x: x + 1

# The keyword: lambda
# A bound variable: x    (an argument to a lambda function.)
# A body: x

# what's the type of lambda in python ?
print type(lambda x: x)
# the result is function, so we can write it this way
print (lambda x: x + 1)(8)
# and it can be named:
my_lambda = lambda x: x + 1
print my_lambda(2)

# more than one arguments:
full_name = lambda first, last: 'full name ' + first + last
print full_name('william', ' x_f_wang')

shang_yushu = lambda x, y: (x / y, x % y)
print shang_yushu(2, 3)

# what about anomyous functions?
# so , In Python, an anomymous funciton is created with the lambda keyword.
# but, more loosely, you can name it
sum = lambda x, y: x + y
print sum(1, 2)

# 2. higher-order functions
# lambda function can be a higher-order function by taking a function(normal or lambda) as an argument
high_ord_func = lambda x, func: x + func(x)
print high_ord_func(2, lambda x: x * x)
print high_ord_func(2, lambda x: x + 3)

# python exposes higher-order functions as built-in functions or in the standard library.
# Examples include map(), filter(), functools.reduce(), as well as key functions like sort(),
# sorted(), min(), and max()


# 3. let's see some difference between function and lambda
add = lambda x, y: x + y
print type(add)
print add

def add(x, y):return x + y
print type(add)
print add


# and let's see some Traceback
# the normal funciton cause a similar error but results in a more precise traceback because it gives the function name
# div_zero = lambda x: x / 0
# div_zero(2)
#
def div_zero(x): return x / 0
div_zero(2)