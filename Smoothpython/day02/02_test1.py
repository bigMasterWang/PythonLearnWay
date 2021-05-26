# -*- coding: utf-8 -*- 
# @Time     : 2020/8/20 9:07 
# @Author   : wangxiaofeng01@corp.netease.com
# @desc:    : 第二章开始

# list可变序列，同时存放不同类型的元素
# 1、list comprehension(列表推导)
# 变为unicode编码
symbols = '$%&*(@'
codes = []
for item in symbols:
    codes.append(ord(item))
print codes
# 列表推导写法，原则
# 只用来创建新的列表，并且尽量保持简短，如果推导代码超过了两行，就要考虑for循环
codes2 = [ord(item) for item in symbols]
print codes2

# 注意变量泄露的问题， x会被覆盖，但是在python3中就不会出现这个问题
x = 'my precious'
dummy = [x for x in 'ABC']
print x

# filter ， sorted, map
# filter:  filter(func, iter)    满足条件返回
# sotred:  sorted(iter, func)    根据fun排序
# map:     map(func, iter)       根据条件转换（映射）

# 用列表推导 和 filter + map  比较
symbols = '$%&*(@'
beyond_ascii = [ord(x) for x in symbols if ord(x) > 20]
print beyond_ascii
beyond_ascii = list(filter(lambda x: x > 20, map(ord, symbols)))
print beyond_ascii
# 上面的例子至少决定说， 列表推导是更加容易理解的，并且效率上甚至比肩filter + map的组合

# 两层（多层嵌套的）列表推导
colors = ['black', 'white']
sizes = ['S', 'M', 'L']

tshirts = [(color, size) for color in colors for size in sizes]
print tshirts
tshirts = [(color, size) for size in sizes for color in colors]
print tshirts

# 列表推导的不足，列表推导只能生成列表，但是不能生成其他类型的序列


# 2、生成器表达式， 实际上就是简写的generator
symbols = '$%&*(@'
# 生成元组, 一次性产出万，不一个一个的拿了
beyond_ascii = tuple(ord(symbol) for symbol in symbols)
print beyond_ascii
# beyond_ascii = (ord(symbol) for symbol in symbols)
# print beyond_ascii.next()

# 生成数组 数组 'i' , 'f' , 'd' , 这是数组，只有数字, 比list效率高
import array
beyond_ascii = array.array('i', (ord(symbol) for symbol in symbols))
print beyond_ascii

# 每次循环拿一个 yield嘛
test_double_generator = ((c, s) for c in colors for s in sizes)
for tshirt in test_double_generator:
    print tshirt


# 元组不仅仅是不可变的列表
class Test(object):
    def __init__(self):
        super(Test, self).__init__()


a = Test()

print a.__class__.__name__
print Test.__name__
