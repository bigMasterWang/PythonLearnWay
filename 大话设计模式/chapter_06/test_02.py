# coding=utf-8
# 更深一步的讨论, python自带decorator


def decorator_func(func):
	def inner(*args, **kwargs):
		print 'decorator_func start'
		func(*args, **kwargs)
		print 'decorator_func end'
	
	return inner


class MyDecorator(object):
	
	def __call__(self, func):
		def inner(*args, **kwargs):
			print '{} in'.format(self.__class__.__name__)
			func(*args, **kwargs)
			print '{} out'.format(self.__class__.__name__)
		return inner


class MyStartEndDecorator(object):
	
	def __call__(self, func):
		def inner(*args, **kwargs):
			with self:
				func(*args, **kwargs)
		
		return inner
	
	def __enter__(self):
		print '{} in'.format(self.__class__.__name__)
	
	def __exit__(self, exc_type, exc_val, exc_tb):
		print '{} out'.format(self.__class__.__name__)


class TargetClass(object):
	
	@MyStartEndDecorator()
	@MyDecorator()
	@decorator_func
	def operation(self):
		print 'I am {}'.format(self.__class__.__name__)


t = TargetClass()
t.operation()

# 执行operation之前, 先执行decorator_func, 这个方法会被当作参数传递进去
# 为什么他的参数会在inner()里面接受?? 没想清楚之前就记清楚返回的内部方法的参数, 就是被修饰方法接受的参数
