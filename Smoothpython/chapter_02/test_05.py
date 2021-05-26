# -*- coding: utf-8 -*- 
# @Time     : 2020/8/27 18:09 
# @Author   : wangxiaofeng01@corp.netease.com
# @desc:    :

"""内存视图 memoryview"""

# 它能让用户在不复制内容的情况下操作同一个数组的不同切片,目前看来还不知道有什么用
# import array
# numbers = array.array('i', [-2, -1, 0, 1, 2])
# print memoryview(numbers)

"""双向队列和其他形式的队列"""
from collections import deque
# 双向队列,在头和尾添加或者删除效率很快
# maxlen是可选参数,代表这个队列可以容纳的元素的数量, 而且一旦设定,这个属性就不能够修改了
dp = deque(range(10), maxlen=10)
print dp
# 对已经满了的队列左
dp.appendleft(-1)
print dp
dp.append(9)
print dp
dp.extend([1, 2, 3])
print dp
# 下面是因为添加的方式是吧添加列表的iter中的元素一个一个的添加到头部,所以造成了逆序的现象
dp.extendleft(reversed([0, 1, 2]))
print dp

# 总结一下方法,
# 1. 创建deque(iterable, maxlen)
# 2. appendleft(number), append(number), pop(number), popleft(number)
# 3. extend(iterable), extendleft(iterable)



# 第二章主要讲的就是序列
# python之禅
# The Zen of Python, by Tim Peters
#
# Beautiful is better than ugly.
# Explicit is better than implicit.
# Simple is better than complex.
# Complex is better than complicated.
# Flat is better than nested.
# Sparse is better than dense.
# Readability counts.
# Special cases aren't special enough to break the rules.
# Although practicality beats purity.
# Errors should never pass silently.
# Unless explicitly silenced.
# In the face of ambiguity, refuse the temptation to guess.
# There should be one-- and preferably only one --obvious way to do it.
# Although that way may not be obvious at first unless you're Dutch.
# Now is better than never.
# Although never is often better than *right* now.
# If the implementation is hard to explain, it's a bad idea.
# If the implementation is easy to explain, it may be a good idea.
# Namespaces are one honking great idea -- let's do more of those!
