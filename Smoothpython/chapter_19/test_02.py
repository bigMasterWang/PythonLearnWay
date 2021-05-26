# -*- coding: utf-8 -*- 
# @Time     : 2021/5/18 21:24 
# @Author   : wangxiaofeng01@corp.netease.com
# @desc:    :

# 使用__new__方法以灵活的方式创建对象
# 这是个类方法,(使用特殊处理, 不必使用@classmethod修饰器), 必须返回一个实例
# 返回的实例会作为第一个参数(即self)传给__init__方法, 因为调用__init__方法时
# 要传入实例, 而且禁止返回任何值, 所以__init__方法其实是"初始化方法", 真正的
# 构造方法是__new__. 我们几乎不需要自己编写__new__方法, 因为从object类继承的实现已经足够了

import keyword
import numbers


class NewFrozenJSON(object):

	def __new__(cls, args):
		if isinstance(args, dict):
			return object.__new__(cls)
		else:
			return args

	def __init__(self, mapping):
		self.__data = {}
		for key, value in mapping.iteritems():
			if keyword.iskeyword(key):
				key += '_'
			self.__data[key] = value

	def __getattr__(self, item):
		# 这个if没有, 也没什么差别
		if hasattr(self.__data, item):
			return getattr(self.__data, item)
		else:
			return NewFrozenJSON(self.__data[item])


x = NewFrozenJSON({'a': {'b': 1}})
print x.a.b


class Record(object):

	# 小技巧,(如果类中没有生命__slots__属性, 那么更新实列的__dict__属性
	# 就能快速地在那个实例中创建一堆属性
	def __init__(self, **kwargs):
		self.__dict__.update(kwargs)

	def __eq__(self, other):
		if isinstance(other, Record):
			return self.__dict__ == other.__dict__
		else:
			return NotImplemented

# x = Record(a=1, b=2)
# print x.a, x.b

# 但是record不能进行递归
dict = {'a': 1, 'b': 2, 'c':{'d': 3}}
x = Record(**dict)
print x.c

class MissingDatabaseError(RuntimeError):
	"""需要数据库但是没有指定数据库时抛出"""

class DbRecord(Record):
	__db = None

	@staticmethod
	def set_db(db):
		DbRecord.__db = db

	@staticmethod
	def get_db():
		return DbRecord.__db

	@classmethod
	def fetch(cls, ident):
		db = cls.get_db()
		try:
			return db[ident]
		except TypeError:
			if db is None:
				msg = 'database not set; call "{}.set_db(my_db)"'
				raise MissingDatabaseError(msg.format(cls.__name__))
			else:
				raise

	def __repr__(self):
		if hasattr(self, 'serial'):
			cls_name = self.__class__.__name__
			return '<{} serial={!r}>'.format(cls_name, self.serial)
		else:
			return super(DbRecord, self).__repr__()


# class Event(DbRecord):
#
# 	@property
# 	def venue(self):
# 		key = 'venue.{}'.format(self.venue_serial)
# 		return self.__class__.fetch(key)
#
# 	@property
# 	def speakers(self):
# 		if not hasattr(self, '_speaker_objs'):
# 			spkr_serials = self.__dict__['speakers']
# 			fetch = self.__class__.fetch

# 实例使用类的方法
# 1. cls.xxx()
# 2. self.__class__.xxx()
# 但是要记住, 即时xxx()是一个类的方法, 使用self.xxx()调用的也是实例的


