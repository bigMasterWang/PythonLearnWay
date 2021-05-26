# -*- coding: utf-8 -*- 
# @Time     : 2021/4/27 17:33 
# @Author   : wangxiaofeng01@corp.netease.com
# @desc:    : 第九章 符合python风格的对象

# 9.6 可散列的Vector2d
# 按照定义, 目前Vector2d实例是不可散列的, 因此不能放入集合(set)中
# 可散列, 需要拿到__hash__值, 还有__eq__方法,

class Vector(object):

	def __init__(self, x, y):
		self.__x = x
		self.__y = y

	# 使用property, 而不写setter可以设置为只读的
	@property
	def x(self):
		return self.__x

	@property
	def y(self):
		return self.__y

	def __str__(self):
		return '( {}, {} )'.format(self.x, self.y)

	def __repr__(self):
		return '( {}, {} )'.format(self.x, self.y)

	# def __hash__(self):
	# 	return hash(self.x) ^ hash(self.y)


v_1 = Vector(1, 2)
v_2 = Vector(3, 4)
print v_1
# v_1.x = 1

test_dict = {
	v_1: '1',
	v_2: '2'
}
print test_dict


# 9.7 私有属性 和 "受保护的"属性
# python有个简单的机制能避免子类意外覆盖"私有"属性
# 1. 改写, 目的是避免意外, 而不能防止故意做错事, 如插销的盖子
# 两个前导下划线, 尾部最多有一个下划线, 命名实例属性, python会把属性名存入实例的的dict属性中, 而且会在前面加上一个下划线和类名
# 如Dog类的__mood, 会变成_Dog__mood

v_3 = Vector(3, 4)
print v_3.__dict__
# print v_3.__x
print v_3._Vector__x

# 一个前导下划线, 受保护的属性

# 9.8 使用__slots__类属性节省空间
# Python在各个实例中名为__dict__的字典里存储实例属性, 为了使用底层的散列表提升访问速度, 字典会消耗大量内存.
# 如果要处理数百万个属性不多的实例, 通过__slot__类属性, 能节省大量内存, 方法是让解释器在元组中存储实例属性, 而不用字典.

# 在类属性中定义__slots__, 然后把他的值设置为一个字符串构成的可迭代对象, 目的是告诉解释器, 这个类中的所有实例属性都在这了
# __slots__是为了优化性能的, 不是为了约束程序员不能添加属性的
# '__dict__' 添加到__slots__中就完全违背了初衷
# '__weakref__' 也要添加到__slots__中
class Vector2d(object):
	__slots__ = ('__x', '__y',)

	def __init__(self, x, y):
		self.__x = x
		self.__y = y

	def __repr__(self):
		return '{} , {}'.format(self.__x, self.__y)


v1 = Vector2d(1, 1)
print v1
# 总之, __slots__能显著节省内存, 不过有几点要注意
# 1. 每个子类都要定义__slots__, 因为解释器会忽略继承的__slots__
# 2. 实例只能拥有__slots_中列出的属性, 除非把'__dict__', 加入__slots__中(这样做就失去了节省内存的功效)
# 3, 如果不把'__weakref__'加入__slots__, 实力就不能作为弱引用的目标
# 如果程序不用处理上百万个实例, 那就别瞎搞了
# NumPy 和 Pandas了解下


# 本章小结:
# 如果使用特殊方法和约定的结构, 定义行为良好且符合python风格的类
# __setattr__和__setattribute__一个是给用户用的, 一个是python用的
# 后一个没找到, 回去第一个里面找找




