# -*- coding: utf-8 -*- 

"""变量作用域规则"""

# b = 2
#
#
# # 在函数中赋值的变量总是局部变量, 比JavaScript在不知情的情况下获取了全局变量好得多哦
# # 除非你使用global
# def f1(a):
# 	print a
# 	print b
# 	b = 3
#
#
# f1(1)

"""闭包"""


class Averager(object):

	def __init__(self):
		super(Averager, self).__init__()
		self.series = []

	def __call__(self, new_value):
		self.series.append(new_value)
		return sum(self.series) / len(self.series)

# 难道不可以把这个看作是一个方法类吗?
# 声明属性, 声明方法
def make_averager():
	series = []

	def averager(new_value):
		series.append(new_value)
		return sum(series) / len(series)

	return averager

a = Averager()
b = make_averager()

print a(1)
print a(2)
print a(3)
print b(1)
print b(2)
print b(3)
print b(4)

#  书上的图很好


# 尝试打印局部变量 和 自由变量
print b.__code__.co_varnames
print b.__code__.co_freevars
# 自由变量真正的
print b.__closure__
print dir(b.__closure__[0])
print b.__closure__[0].__class__
print b.__closure__[0].cell_contents


print b.__code__.co_filename



# 一个闭包的bug
# 新的效率更高的闭包
# def make_averager_two():
# 	count = 0
# 	total = 0
#
# 	def averager(new_value):
# 		count += 1
# 		total += new_value
# 		return total / count
#
# 	return averager

# 上面的这种写法就是错误的, 因为count += 1 实际上就是 count = count + 1
# 实际上是给count赋值了, 那么这回把count变成局部变量, 之前列表可以是因为列表是可变对象
# python3中可以像global一样, 声明nonlocal, 但是python2中没有, 那么就是用如下的方法
def make_averager_two():
	a = {'count': 0, 'total':0}

	def averager(new_value):
		a['count'] += 1
		a['total'] += new_value
		return a['total'] / a['count']

	return averager

x = make_averager_two()
print x(2)
print x(3)
print x(4)
print x(5)
print x(6)
print x(7)
print x(8)

