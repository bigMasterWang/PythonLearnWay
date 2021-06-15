# 第十五章, 就不能不换DB吗?——抽象工厂模式


# =============================================基础版本================================================
class User:

	def __init__(self, id, name):
		self._id = id
		self._name = name


class SqlserverUser:

	def insert(self, user):
		print('sqlserver insert a user: {}'.format(user))

	def get_user(self, id):
		print('get user by id: {}'.format(id))


# ============================================工厂方法模式版本=================================================


from abc import ABC, abstractmethod


class SqlUser(ABC):

	@abstractmethod
	def insert(self, u):
		pass

	@abstractmethod
	def get_user(self, id):
		pass


class MySqlUser(SqlUser):

	def get_user(self, id):
		print('get_user: {} '.format(self.__class__.__name__))

	def insert(self, u):
		print('insert: {} '.format(self.__class__.__name__))


class OracleSqlUser(SqlUser):

	def insert(self, u):
		print('get_user: {} '.format(self.__class__.__name__))

	def get_user(self, id):
		print('insert: {} '.format(self.__class__.__name__))


class SqlFactory(ABC):

	@abstractmethod
	def get_user(self):
		pass

	@abstractmethod
	def get_department(self):
		pass


class MySqlFactory(SqlFactory):

	def get_user(self):
		return MySqlUser()

	def get_department(self):
		return


class OracleFactory(SqlFactory):

	def get_user(self):
		return OracleSqlUser()

	def get_department(self):
		pass


def test_01():
	# 最开始的一版本, 完全没有任何模式, 换db就要直接重来
	u1 = User(1, 'william')
	sql_u = SqlserverUser()
	sql_u.insert(u1)
	u2 = sql_u.get_user(2)


def test_02():
	# 这个使用工厂方法模式, 只改变sql_factory就行了, 其他的接口用法都是一样的
	# 但是即使这样, 如果要更换db, 还是要将sql_factory = MySqlFactory()改成sql_factory = OracleFactory()
	u = User(1, 'william')
	# sql_factory = MySqlFactory()
	sql_factory = OracleFactory()
	sql_user = sql_factory.get_user()
	sql_user.insert(u)
	sql_user.get_user(2)


class Department(ABC):

	@abstractmethod
	def get_department(self, id):
		pass

	@abstractmethod
	def insert(self, u):
		pass


class MySqlDepartment(Department):
	def get_department(self, id):
		print('get_department: {} '.format(self.__class__.__name__))

	def insert(self, u):
		print('insert: {} '.format(self.__class__.__name__))


class OracleDepartment(Department):
	def get_department(self, id):
		print('get_department: {} '.format(self.__class__.__name__))

	def insert(self, u):
		print('insert: {} '.format(self.__class__.__name__))


def test_03():
	# 如果要新加一张表, 比如department表
	# 那么就要建立新的一个基类和两个不同数据库的子类
	# 然后还要在factory中建立新的get_department的方法, 子类也都要修改
	# 这里就吧这两个department的类写好, factory基类的写好, 其余的就不写了
	pass


# if __name__ == '__main__':
# 	# test_01()
# 	test_02()


# 抽象工厂模式

# 抽象工厂模式: 提供一个创建一系列相关或相互依赖对象的接口, 而无需指定它们具体的类
# 好处,
# 1. 向上面的, 只需要改变最开始初始化抽象工厂的地方, 其余的地方就不需要进行更改了
# 2. 客户端只需要知道user和department类

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# 演变过程:
# 主要就是为了选择不同的具体操作类
# 简单工厂模式, 通过建立一个工厂类, 在工厂类里面通过switc判断到底需要产生哪一个类的实例
# 抽象工厂模式, 通过建立一个工厂的基类, 然后不同的目标类都有自己专属的工厂子类, 这样就避免了switch(实际上是switch移动到客户端程序了)
# 用反射技术解决switch问题, 那么只需要一个factory类, 接收要创建的class类就行了
# 但是困难在于, 怎么知道那class的名字????, 还不是要进行判断??? 可能是客户端进行判断吧
# 所以对于工厂模式, 不要过于深究, 因为根本没办法避免判断

# python的反射
# 本地的, 其实import之后就已经到本地的globals了
# print(globals()['User'](1, 'william'))
# 其他文件额度
# mod = __import__('test2')
# print(getattr(mod, 'User2'))
class A:

	def __init__(self, name):
		self.name = name


class B:

	def __init__(self, name):
		self.name = name


class ReflectionFactory:

	def create_class(self, class_name):
		return globals()[class_name]


r = ReflectionFactory()
a = r.create_class('A')('william')
print(a.name)


# 重写计算器

class Operation(ABC):

	@abstractmethod
	def get_result(self, a, b):
		pass


class AddOperation(Operation):
	def get_result(self, a, b):
		return a + b


class SubOperation(Operation):
	def get_result(self, a, b):
		return a - b


class MulOperation(Operation):
	def get_result(self, a, b):
		return a * b


class DivOperation(Operation):
	def get_result(self, a, b):
		return a / b



class OperationFactory:

	@staticmethod
	def create_operation(operation_name, *args, **kwargs):
		return globals()[operation_name](*args, **kwargs)


if __name__ == '__main__':

	# 没办法不做判断, 因为输入的根本不是类名,除非提前写好
	# 很像配置文件
	class_name_dict = {
		'+': 'AddOperation',
		'-': 'SubOperation',
		'*': 'MulOperation',
		'/': 'DivOperation',
	}

	number_a = int(input('please input a\n'))
	number_b = int(input('please input b\n'))
	operation = input('please input operation + | - | * | /\n')
	op = OperationFactory.create_operation(class_name_dict[operation])
	print(op.get_result(number_a, number_b))

