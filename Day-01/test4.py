# coding=utf-8
# # decorator
#
# # prerequires:everything in python is object even function,attributes,variables,params
#
# def inc(x):
#     return x + 1
#
#
# def dec(x):
#     return x - 1
#
#
# def operation(func, x):
#     return func(x)
#
#
# print(operation(inc, 1))
#
#
# # decorator example
# def make_pretty(func):
#     def inner():
#         print("I got decorated")
#         func()
#
#     return inner
#
#
# def ordinary():
#     print("I am ordinary")
#
#
# pretty = make_pretty(ordinary)
# pretty()
#
# print(pretty.__closure__[0].cell_contents)


# pretty()

# so add the @make_pretty to ordinary() is same to ordinary = make_pretty(ordinary)

# example two:
#
# def smart_divide(func):
#     def inner(a, b):
#         print("I am going to divide ", a, "and", b)
#         if (b == 0):
#             print("Whoops! cannot divide")
#             return
#         return func(a, b)
#
#     return inner
#
#
# @smart_divide
# def divide(a, b):
#     return a / b
#
#
# print(divide(1, 2))
# print(divide(1, 0))
# #
#
# def works_for_all(func):
#     def inner(*args, **kwargs):
#         print("I can decorator any function")
#         return func(*args, **kwargs)
#
#     return inner
#
#
# 来看看一个有意思的例子
def father_protect(func):
    def inner(*args, **kwargs):
        print("F" * 30)
        func(*args, **kwargs)
        print("F" * 30)

    return inner


def mother_protect(func):
    def inner(*args, **kwargs):
        print("M" * 30)
        func(*args, **kwargs)
        print("M" * 30)

    return inner

@father_protect
@mother_protect
def child(msg):
    print(msg)

child("I am save")

#child = father_protect(mother_protect(child))
#child("Hello")
