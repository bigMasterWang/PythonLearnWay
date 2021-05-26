# coding=utf-8
# test_list = [1, 2, 3, 4]
#
# test_iter = iter(test_list)
#
# print(next(test_iter))
# print(next(test_iter))
# print(test_iter.__next__())
# print(test_iter.__next__())
# print(test_iter.__next__())

# When we reach the end and there is no more data to be returned,
# it will raise StopIteration.
# raise StopIteration
# next(test_iter)


# # 手动实现for loop
# test_list_two = ["123", "456", "789"]
# for item in test_list_two:
#     print(item)
# # for loop 的大致原理
# # a for loop takes an iterator and iterates over it using next()
# test_iter = iter(test_list_two)
# while True:
#     try:
#         print(next(test_iter))
#     except StopIteration:
#         break


# next和iter也只不过是调用的实例的self.__next__,和self.__iter__而已
# # 至于for loop的内部原理是不是这样呢？我们可以做一个实验
# class TestIterator:
#     def __init__(self, max):
#         self.max = max
#
#     def __iter__(self):
#         self.n = 0
#         return self
#
#     def __next__(self):
#         if self.n < self.max:
#             result = 3 ** self.n
#             self.n += 1
#             return result
#         else:
#             raise StopIteration
#
#
# a = TestIterator(4)
#
# for item in a:
#     print(item)

# 不过要小心，因为循环使用的无限续循环，迭代对象很有可能永远了无法耗尽
# 如下面的例子，int()是可迭代的，然后iter()方法里面第二个参数是哨兵
# 意思就是如果next值不是第二个参数，就继续迭代
# test_iter = iter(int, 1)
# print(test_iter.__next__())
# print(test_iter.__next__())
# print(test_iter.__next__())
# print(test_iter.__next__())
# print(test_iter.__next__())
# print(test_iter.__next__())
# print(test_iter.__next__())
# print(test_iter.__next__())
# print(test_iter.__next__())
#
# 我们也可以手动让for循环无线循环，只要raise StopIteration就行了
class TestIteratorTwo:

    def __iter__(self):
        self.num = 1
        return self

    def __next__(self):
        num = self.num
        print(num)
        self.num += 2
        return num


# 这样就无限循环了，看吧，即使是for循环里面pass了，也是有输出的
for item in TestIteratorTwo():
    pass