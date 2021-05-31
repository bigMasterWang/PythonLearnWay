
# 第十二章 牛市股票还会亏钱?——外观模式
# 外观模式: 为子系统的一组接口提供一个一致的界面,此模式定义了一个高层接口,这个接口使得这一子系统更加容易维护

# 外国类需要了解所有子系统的方法和属性,进行组合,以备外界调用

class SubSystemOne:

	def method_one(self):
		print(self.__class__.__name__, 'method_one')


class SubSystemTwo:

	def method_two(self):
		print(self.__class__.__name__, 'method_two')


class SubSystemThree:

	def method_three(self):
		print(self.__class__.__name__, 'method_three')


class SubSystemFour:

	def method_four(self):
		print(self.__class__.__name__, 'method_four')


class Facade:

	def __init__(self):
		self.one = SubSystemOne()
		self.two = SubSystemTwo()
		self.three = SubSystemThree()
		self.four = SubSystemFour()

	def method_a(self):
		self.one.method_one()
		self.two.method_two()

	def method_b(self):
		self.three.method_three()
		self.four.method_four()


if __name__ == '__main__':
	facade = Facade()
	facade.method_a()
	facade.method_b()


# 何时使用外观模式
# 分为三个阶段
# 首先,在设计初期阶段, 应该要有意识的将不同的两个层分离(比如MVC)
# 其次,在开发阶段,子系统往往因为不断的重构演化而变得越来越复杂, 增加外观Facade可以提供一个简单的接口,减少
#      减少他们之间的依赖
# 第三, 在维护一个遗留的大型系统时,可能这个系统已经非常难以维护和扩展了, 为新系统开发一个外观Facade类,来提供
#      射击粗糙或者高度复杂的遗留代码的比较清晰简单的接口,让新系统与Facade对象交互,Facade与遗留代码交互所有复杂的工作
