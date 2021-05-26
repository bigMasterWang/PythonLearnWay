# -*- coding: utf-8 -*- 
# @Time     : 2020/8/25 9:41 
# @Author   : wangxiaofeng01@corp.netease.com
# @desc:    :

"""1、对序列使用+和*"""
# * 是把序列复制几份再拼接起来， 如果l是可变对象的引用， 那么得到的只是几个引用指向
# 同一个对象罢了
l = [1, 2, 3]
print l * 5
print 5 * 'abcd'
# + 和 * 一样，不改变原有的操作对象，而是构建一个全新的序列


"""2、建立由列表组成的列表"""
# 初始化一个嵌套着几个列表的列表， 最好的选择是使用列表推导
board = [['0'] * 3 for i in range(3)]
print board
board[1][1] = '1'
print board

# 一种错误的方式，但是写法上很漂亮，但是是错误的, 引用指向的是同一个对象
wrong_board = [['0'] * 3] * 3
print wrong_board
wrong_board[1][1] = '1'
print wrong_board
# 上面的错误其实和下面的一样
row = ['0'] * 3
board = []
for i in range(3):
    board.append(row)
print board
board[1][1] = '1'
print board

"""3、序列的增量赋值 += , *="""
l = [1, 2, 3]
print id(l)
l *= 2
print id(l)  # 同一个id

t = (1, 2, 3)
print id(t)
t *= 2
print id(t)  # 不是同一个id
# 变量名有没有关联到新的对象，完全取决于这个类型有没有实现__iadd__这个方法，实现了就是append，是同一个对象

l = [1, 2, 3]
print id(l)
l += [4, 5]
print id(l)

# 其实下面的报错中，TypeError抛出了，但是内容也改变了
t = (1, 2, [30, 40])
print id(t)
# t[2] += [50, 60]  # 这一句可以指，这种错误是极为少见的
# t[2].extend([50, 60])   # 这样写就能避免TypeError的异常
print id(t)
print t


# 1、不要把可变对象放在元组里面
# 2、增量赋值不是一个原子操作


"""3、list.sort方法和内置函数sorted"""
# sort是就地改变，sorted是新建一个列表，一个返回None，一个返回新建列表
# 他们都有两个可选的关键字参数，reverse， key：一个只有一个参数的函数，
fruits = ['grape', 'raspberry', 'apple', 'banana']
print sorted(fruits, key=len)
fruits.sort()
print fruits


class TestClass(object):
    def __init__(self, value):
        super(TestClass, self).__init__()
        self.a = value

    def __repr__(self):
        return "a=" + str(self.a)


x = [TestClass("1"), TestClass('123'), TestClass("1234"), TestClass("12345")]

print sorted(x, key=lambda any: len(any.a), reverse=True)

# cmp用的是+-返回值， 而key是用什么键来比较，默认是升序的
x.sort(cmp=lambda x, y: len(y.a) - len(x.a))
print x

"""4、用bisect来管理已排序的序列"""
# bisect和insort
# import bisect
#
# HAYSTACK = [1, 4, 5, 6, 8]
# NEEDLES = [0, 1, 2, 5, 10]
# ROW_FORMAT = '{0:2d}    @  {1:2d}   {2}{0:<2d}'
#
# def demo(biesct_fn):
#     for needle in reversed(NEEDLES):
#         position = biesct_fn(HAYSTACK, needle)
#         offset = position * '   |'
#         print ROW_FORMAT.format(needle, position, offset)
#
# print 'DEMO:'
# print 'hasystack  ->  ', '  '.join('%2d' % n for n in HAYSTACK)
# demo(biesct_fn=bisect.bisect_right)


# bisect.bisect == bisect.bisect_right

# bisect.insort(list, item) 在list是升序的情况下，直接有序的插入一个item
import bisect
import random

random.seed(1729)
test_list = []

for i in range(7):
    new_item = random.randrange(start=0, stop=14)
    bisect.insort_left(test_list, new_item)
    print '{0:2d} -> {1}'.format(new_item, test_list)


"""5、当列表不是首选时"""
# 大概意思就是说如果列表中都是数字的话，array可能效率更好一些，并且频繁的对数组
# 进行先进先出的操作时，deque的速度应该会更快

"""6、数组"""
# 如果要创建一个只包含数组的列表,array.array比list更加高效
# 但是创建数组需要类型码
# 已经下载了图片,常用的'b','i','f','d'
from array import array
from random import random
floats = array('d', (random() for i in range(10**7)))
print floats[-1]

# open的使用"https://www.runoob.com/python/file-methods.html"
fp = open('test.txt', 'wb')
floats.tofile(fp)
fp.close()
floats2 = array('d')
fp = open('test.txt', 'rb')
floats2.fromfile(fp, 10**7)
fp.close()
print floats2[-1]
print floats2 == floats

# 给数组排序,就需要新建一个数组了,但是在有序的情况下加入,bisect.insort还是能派上用场的
a = array(floats.typecode, sorted(floats))
# a = sorted(floats)
# print a[-1]
