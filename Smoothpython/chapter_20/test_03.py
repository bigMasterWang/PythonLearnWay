# -*- coding: utf-8 -*- 
# @Time     : 2021/5/24 19:18 
# @Author   : wangxiaofeng01@corp.netease.com
# @desc:    :
import abc

# LineItem类第5版, 一种新型描述符


class AutoStorage(object):
	_counter = 0

	def __init__(self):
		cls = self.__class__
		prefix = cls.__name__
		index = cls._counter
		self.storage_name = '_{}#{}'.format(prefix, index)
		cls._counter += 1

	def __get__(self, instance, owner):
		if instance is None:
			return self
		else:
			return getattr(instance, self.storage_name)

	# 这个是基础
	def __set__(self, instance, value):
		setattr(instance, self.storage_name, value)


class Validated(AutoStorage):
	@abc.abstractmethod
	def validate(self, instance, value):
		"""return validated value or raise ValueError"""

	# 这个是扩展
	def __set__(self, instance, value):
		value = self.validate(instance, value)
		super(Validated, self).__set__(instance, value)


class Quantity(Validated):

	def validate(self, instance, value):
		if value >= 0:
			raise ValueError('value must be > 0')
		return value


class NonBlank(Validated):

	def validate(self, instance, value):
		value = value.strip()
		if len(value) == 0:
			raise ValueError('value cannot be empty or blank')
		return value



# 应用
class LineItem(object):
	description = NonBlank()
	weight = Quantity()
	price = Quantity()

	def __init__(self, description, weight, price):
		self.description = description
		self.weight = weight
		self.price = price

	def subtotal(self):
		return self.weight * self.price


# 实例属性可以覆盖__set__()描述符
# 没有写__get__()时, 会去实例的__dict__去获取
# 别忘了还有__delete__()虽然没有任何用

# 不管描述符是不是覆盖型, 为类属性赋值都能覆盖描述符

# 用法建议
# 1. 使用特性以保持简单, 就是使用@property
# 2. 只读描述符必须实现__set__, 然后在里面抛出异常
# 3. 用于验证的描述符可以只有__set__方法, 然后直接在__dict__中设置属性
# 4. 仅有__get__方法可以实现高效缓存, 执行某些耗费资源的计算, 然后为实例设置同名属性, 缓存结果
# 		同名实例属性会覆盖描述符, 因此后续访问会直接从__dict__属性中获取值, 而不会在出发描述符的__get__方法
