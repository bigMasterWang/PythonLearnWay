# -*- coding: utf-8 -*- 
# @Time     : 2021/5/6 19:36 
# @Author   : wangxiaofeng01@corp.netease.com
# @desc:    :

# 散列和快速等值测试
# reduce
import functools
print functools.reduce(lambda x, y: x*y, range(1, 6, 1))

# operator模块以函数形式提供了python的全部中缀运算符, 从而减少使用lambda表达式
import operator
print functools.reduce(operator.xor, range(1, 6, 1))


# 归约 reduce, sum, any, all 把序列或有限的可迭代对象编程一个聚合结果
# 映射归约: 把函数应用到各个元素上, 生成一个新序列(映射, map), 然后计算聚合值(归约, reduce)
hashs = map(hash, range(1, 11, 1))
res = functools.reduce(lambda x,y: x*y, hashs)
print res

# 出色的zip函数
test = zip(range(3), 'ABC')
print type(test)

# 看看这个
my_list = [[1, 2, 3], [40, 50, 60], [9, 8, 7]]
res = functools.reduce(lambda a, b: a+b, [sub[1] for sub in my_list])
print res
res = functools.reduce(lambda a, b: a+b[1], my_list, 0)
print res
# 最标准的
res = sum(sub[1] for sub in my_list)
print res