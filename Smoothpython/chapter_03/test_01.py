# -*- coding: utf-8 -*- 
# @Time     : 2020/8/29 15:53 
# @Author   : wangxiaofeng01@corp.netease.com
# @desc:    : 第三章 "字典和集合"

"""3.1 泛映射类型"""
import collections

my_dict = {}
# print isinstance(my_dict, collections.Mapping)
# 在python 2.6及其之前 dict都属于collections.Mapping中
# 而之后属于collections.abc.MutableMapping

"""3.1. 只有可散列的数据类型才能作为这些映射里的键"""
# 如果一个对象是可散列的,那么这个对象的生命周期中,它的散列值是不变的
# 而且这个对象需要实现__has__()方法,另外还要有__qe__()方法,这样才能比较
# 原子不可变的数据类型都是可散列的(str, bytes, 和 数值类型),元组的话只有当一个元组包含的所有元素都是可散列的,他才是可散列的
# 如下例子
tt = (1, 2, (30, 40))
# print hash(tt)
# tl = (1, 2, [30, 40])
# print hash(tl)
# TypeError: unhashable type: 'list'

# hash和id有什么区别?
a = '123'
# print hash(a)
# print id(a)

"""3.2 字典推导"""
DIAL_CODES = [
    (86, 'China'),
    (91, 'Indian'),
    (1, 'United States'),
    (62, 'Indonesia'),
    (55, 'Brazil'),
    (92, 'Pakistan'),
    (880, 'Bangladesh'),
    (234, 'Nigeria'),
    (7, 'Russia'),
    (81, 'Japan')
]
# print DIAL_CODES
country_code = {country: code for code, country in DIAL_CODES}
# print country_code
# print {code: country.upper() for code, country in DIAL_CODES if code <= 86}


"""3.3 常见的映射方法"""
# 处理找不到的键
# 1. 用get(key, default)代替d[k]
test_dict = {1: '1', 2: '2'}
item = test_dict.get(2, None)
print test_dict
print item
# 2. 用setdefault处理找不到的键(如果要更新某个键对应的值的时候,不管使用__getitem__还是get都会不自然,而且效率低)
# 若字典里有键,则把他的值设置为default,然后返回这个值,若无,则让d[k] = default,然后返回default
print test_dict.setdefault(1, 'hello world')
print test_dict
# 上面的好像不仅不能在python2.7中正确运行,而且直接使用test_dict[] = default难道不是同样的效果吗???
# 并且找的时候使用get(key,default)不就行了吗?
# 上面的写法不美, 不符合python之禅第一句 "Beautiful is better than ugly."

"""3.4 给找不到的键返回一个默认值"""
# 方法一,使用get(key, default)方法
x = test_dict.get(3, 123)
print x
# 方法二,使用defaultdict处理, 初始化的时候给一个默认返回值的类型,如果是str就返回空串
# 如果是bool,找不到键就返回False,如果写None,就会报错,如此傻逼,我选择不用
import collections

s = [(1, '1'), (2, '2')]
test_dict = collections.defaultdict(str)
for k, v in s:
    test_dict[k] = v
print test_dict[3] == ''

"""3.4 __missing__"""


# 这TMD不是好用多了,我就只需要在找不到值的时候给我一个默认返回值
# dict[key] 调用的是 __getitem__(), 如果没有,就调用__missing__()
# 并且__missing__只由__getitem__()调用
class MyDefualtDict(dict):
    def __missing__(self, key):
        return None


x = MyDefualtDict()
x[1] = 1
print x[1]
print x[2]
print 2 in x
print x.get(2, '1')
# 总结一下dict常用的方法
# dict[] 调用的是__getitem__(self, key)
# get() 调用的就是get(self, key, default=None)
# key in dict 调用的是 __contains__(self, key)
# __missing__()找不到时会调用,dict[]会直接调用,get()在没有传入default时会调用


"""3.5 字典的变种"""
# 我目前的能力不用看

"""3.6 子类化UserDict"""
# 要么是我目前能力不足,要么是脱了裤子放屁

"""3.7 不可变映射类型"""
# 讲的都是python3的,略过

"""3.8 集合论"""
# set frozenset
l = ['spam', 'spam', 'eggs', 'spam']
print l
# 集合去重
l = list(set(l))
print l

# 中缀运算符 交集 & , 合集 | , 差集 -
x = [1, 2, 3, 4]
y = [4, 5, 6, 7]
print set(x) | set(y)
print set(x) & set(y)
print set(x) - set(y)

# 集合中的类存储的不是__hash__()
# 是id吗?
class TestSet(object):
    def __init__(self, value):
        super(TestSet, self).__init__()
        self.value = value

    def __hash__(self):
        return self.value


x = [TestSet(1), TestSet(2), TestSet(3), TestSet(4)]
y = [TestSet(4), TestSet(5), TestSet(6), TestSet(7)]
x = [item.value for item in x]
y = [item.value for item in y]
print x
print y
print set(x) & set(y)


"""3.8 集合字面量"""
# 空集必须写成set(), {}是空字典, 语法陷阱
x = {1, 2, 3}
y = set()
print x | y

"""3.8 集合推导"""
# unichr(i) 得到字符的名字
from unicodedata import name
x = {unichr(i) for i in range(1, 256) if 'SIGN' in name(unichr(i), '')}
print x


"""3.8 集合的操作"""
# 就是一些基本的集合操作
x = {1, 2, 3, 4, 5}
y = {5, 6, 7, 8, 9}
z = [4, 5, 6]
# 1 交集
# 1.1 a & b  =>  a.__and__(b)    =>  a.intersection(iter,...)
# set([5])
print x & y
# set([5])
print x.__and__(y)
# set([4, 5])
print x.intersection(z)
# 1.2 a &= b    =>  a.__iand__(b)   => a.intersection_update(iter,...)
x.intersection_update(z)
print x

# 2 并集
# 2.1 a | b =>  a.__or__(b) =>  a.union(iter,...)
# 2.2 a |= b    =>  a.__ior__(b)    =>  a.update(iter,...)

# 3 差集
# 3.1 a - b =>  a.__sub__(b)    =>  a.difference(iter,...)
# 3.2 a -= b    =>  a.__isub__(b)   =>  a.difference_update(iter,...)


# 属于 e in a    => a.__contains__(e)
# 子集 a <= b     ->      a.__le__(b)         ->      a.issubset(iter)
# 真子集 a < b     ->      a.__lt__(b)
# 父集 a >= b     ->      a.__ge__(b)     ->      a.issuperset(iter)
# 真父集 a > b    ->       a.__gt__(b)


"""3.9 dict和set的背后"""
# dict和set查询的时间几乎是可以忽略不见的
# 1000w中找1000个, dict 0.000337s, set的& 0.000314, list的in 97.948
# 原因就在于散列表
# x in list 速度是远远不如 x & y的

"""3.9 字典中的散列表"""
# 1. dict中散列表的表元(key引用, value引用),会保证1/3是空的,快要达到阈值时就复制到更大的空间中
# 2. my_dict[key]中,首先用hash(key)计算散列值,然后用最低的几位数字当作偏移量,直接去找(为空keyError,不为空,且target_key==key,返回)
# 3. 如果KeyError,再多取几位,用特殊方法处理一下,当作索引再次寻找

# 和java的 hash数组 + 解决冲突(红黑树/ B+数 / 顺延等) 思路基本一致
# 不过是改成了 散列表(hash()) + 解决冲突(循环取值)


"""3.9 dict的实现及其导致的结果"""
# 1. 键必须是可散列的
#       1.1 支持hash(),并且通过__hash__()得到的散列值是不变的
#       1.2 支持通过__eq__()方法来检查相等
#       1.3 若 a == b为真, 则hash(a) == hash(b)也为真
# 看上面的陈述也就明白了, __eq__()调用的是hash

# 前提
# 1. id是内存, 跟is有关      hash是值,跟==有关(可散列的,hash不能变)
# 2. 重要的几个方法: __hash__(),    ==,   __eq__()
# 3. 用户自定义的两个类的散列值用的是id,__eq__和==用的都是id,也就是hash完全被id取代了,自定义的类所以都是可散列的
# 4. __eq__是dict中判断 散列表中的key 和 传进来的key 是不是相同的方法
# 可散列的

# 支持hash(),并且通过__hash__()得到的散列值是不变的,所以 == 相等, hash()也要相等,这是值相等,并且hash是不可变的
# 也就是说hash必须跟值挂钩,但是值改变,hash值并不改变
# 所以set是不可改变的,列表可变但是没有hash,
# 自定义的类可散列,但是用的全是id,永远不可能出现 == 和 hash() == hash()的情况
# 如下例子最能说明
a = (1, 2, 3)
b = (1, 2, 3)
print id(a)
print id(b)
print a == b
print a.__eq__(b)
print hash(a), hash(b)

test_dict = {}

test_dict[a] = '123'
print test_dict[a]
print test_dict[b]
# 所以python走了两个极端
# 1.像set,hash跟值相关,但是不能改变,干脆不让值改变不就行了,str,int都是如此,只不过set值改变时会报错,更容易观察,而str,int改变了之后就不是
#       之前的对象了,是默认进行的
# 2.像自定义类,干脆散列值直接用id,不用hash,所以你值随便变动,但是id内存地址是不变的,也是满足可散列的
#
# 问题就在于 == 判断时用的是hash

class TestClass(object):
    def __init__(self, value):
        self._value = value
    def __hash__(self):
        return self._value
    def __eq__(self, other):
        return self._value == other._value
    #    return self.__hash__() == other.__hash__()
    #     return id(self) == id(other)
    #     return True

a = TestClass(1)
b = TestClass(1)
c = TestClass(1)
test_dict[a] = '1'
print a == b == c
print test_dict[a], test_dict[b], test_dict[c]

# 在上面的例子中,我们只要让值不能改变即可完全满足可散列的条件


# 下面这三句话值1000块钱
# 1. 传入key寻找在散列表中的位置的时候,用的是hash
# 2. 找到位置判断是否相等时,用的是== ,而python中 == 调用的是__eq__
# 外加hash跟值相关,只不过自定义的类,不重写__eq__()调用的都是id罢了

