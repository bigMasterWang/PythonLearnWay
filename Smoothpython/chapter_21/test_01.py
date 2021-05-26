# -*- coding: utf-8 -*- 
# @Time     : 2021/5/24 20:36 
# @Author   : wangxiaofeng01@corp.netease.com
# @desc:    : 类元编程

# 564

def record_factory(cls_name, field_names):
	try:
		field_names = field_names.replace(',', ' ').split()
	except AttributeError:
		pass
	field_names = tuple(field_names)

	def __init__(self, *args, **kwargs):
		# __slots__在下面dict里面就已经赋值了, 就是上面的field_names
		attrs = dict(zip(self.__slots__, args))
		attrs.update(kwargs)
		for name, value in attrs.iteritems():
			setattr(self, name, value)

	def __iter__(self):
		for name in self.__slots__:
			yield getattr(self, name)

	# slots => tuple(field_names, ...)
	cls_attrs = dict(__slots__=field_names, __init__=__init__, __iter__=__iter__)

	return type(cls_name, (object,), cls_attrs)

x = record_factory('Dog', 'name, age')
print x
x.name = '567'
print x.name

# 上面创建的类不能进行序列化

# test = type('Test', (object, ), dict(__slots__=tuple(['a', 'b'])))
# print test
# test.a = 1
# print test.a
