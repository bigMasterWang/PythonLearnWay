# generator

# the differences between Generator function and a Normal function:
#
# 1、Generator函数包含一个 yield语句
# 2、当调用这个函数的时候，并不立即执行，而是返回一个iterator
# 3、 __iter__()和__next__()等iterator必须包含的函数都是自动实现的
# 4、 一旦Generator函数执行，这个函数就会暂停在yield的位置，线程的执行权交给函数
#       的调用者
# 5、 执行结束的时候，会自动raise StopIteration的异常

# def my_gen():
#     n = 1
#     print("this is the first print")
#     yield n
#
#     n += 1
#     print("this is the second print")
#     yield n
#
#     n += 1
#     print("this is the third print")
#     yield n
#
#
# for item in my_gen():
#     print(item)
#
# b = my_gen()
# b.__next__()
# b.__next__()
# b.__next__()

#
# # Normally, generator functions are implemented with a loop having a suitable terminating condition.


# def rev_ste(my_str):
#     length = len(my_str)
#     for i in range(length - 1, -1, -1):
#         print(my_str[i])
#         yield my_str[i]
#
#
# for char in rev_ste("hello"):
#     pass
#
#
# Similar to the lambda functions which create anonymous functions,
# generator expressions create anonymous generator functions.
#
# The major difference between a list comprehension and a generator expression is that
# a list comprehension produces the entire list while the generator expression produces one item at a time.
# 更少的内存使用，比等价的列表要好的多啊
# They have lazy execution ( producing items only when asked for ).
# For this reason, a generator expression is much more memory efficient than an equivalent list comprehension.
#
#
# my_list = [1, 2, 3, 4]
# list_ = [x ** 2 for x in my_list]
# generator = (x ** 2 for x in my_list)
#
# print(list_)
# print(generator)
#
# for x in generator:
#     print(x)
#
# Generator expressions can be used as function arguments.
# When used in such a way, the round parentheses can be dropped.
#
# my_list = [1, 2, 3, 4]
# print(sum(x ** 2 for x in my_list))
# print(max(x ** 2 for x in my_list))
#
#
# def my_test_method(max):
#     for i in range(0, max, 1):
#         yield 2 ** i
#
#
# for item in my_test_method(10):
#     print(item)
#
#
# Why generators are used in Python?
# 1. Easy to Implement
# 2. Memory Efficient(A normal function to return a sequence will create the entire sequence
#    in memory before returning the result.
#    This is an overkill, if the number of items in the sequence is very large.
#    Generator implementation of such sequences is memory friendly
#    and is preferred since it only produces one item at a time.)
# 3. Represent Infinite Stream
# 4. Pipelining Generators
#
def fibonacci_numbers(nums):
    x, y = 0, 1
    for _ in range(nums):
        x, y = y, x + y
        yield x


def square(nums):
    for num in nums:
        yield num ** 2


print(type(fibonacci_numbers(10)))
print(type(square(fibonacci_numbers(10))))
print(sum(square(fibonacci_numbers(10))))

#
# # 主要是少占内存
#


