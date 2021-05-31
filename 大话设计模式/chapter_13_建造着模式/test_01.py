# 第十三章 好菜每回味不同——建造者模式
# 建造者模式将一个复杂对象的构建与它的表示分离,是的同样的构建过程可以创建不同的表示
# 主要解决的就是流程标准化, 做菜忘记放盐, 画人忘记画腿

# 将一个复杂对象的构建与它的表示分离,使得同样的构建过程可以创建不同的表示, '建造者模式'又叫生成器模式.
# 如果我们用了建造者模式,那么用户就只需指定需要建造的类型就可以得到他们,而具体的建造的过程和细节就不知道了

# director:指挥者, 使用构建对象接口的对象
# builder: 构建者基类
# ConcreteBuilder: 具体的建造者, 产出结果
from abc import ABC, abstractmethod


class PersonBuilder(ABC):

	@abstractmethod
	def build_head(self):
		pass

	@abstractmethod
	def build_body(self):
		pass

	@abstractmethod
	def build_right_arm(self):
		pass

	@abstractmethod
	def build_left_arm(self):
		pass

	@abstractmethod
	def build_right_leg(self):
		pass

	@abstractmethod
	def build_left_leg(self):
		pass


class FatPerson(PersonBuilder):

	def build_head(self):
		print('构建 {} 的头'.format(self.__class__.__name__))

	def build_body(self):
		print('构建 {} 的身体'.format(self.__class__.__name__))

	def build_right_arm(self):
		print('构建 {} 的右臂'.format(self.__class__.__name__))

	def build_left_arm(self):
		print('构建 {} 左臂'.format(self.__class__.__name__))

	def build_right_leg(self):
		print('构建 {} 的右腿'.format(self.__class__.__name__))

	def build_left_leg(self):
		print('构建 {} 的左腿'.format(self.__class__.__name__))


class LeanPerson(PersonBuilder):

	def build_head(self):
		print('构建 {} 的头'.format(self.__class__.__name__))

	def build_body(self):
		print('构建 {} 的身体'.format(self.__class__.__name__))

	def build_right_arm(self):
		print('构建 {} 的右臂'.format(self.__class__.__name__))

	def build_left_arm(self):
		print('构建 {} 左臂'.format(self.__class__.__name__))

	def build_right_leg(self):
		print('构建 {} 的右腿'.format(self.__class__.__name__))

	def build_left_leg(self):
		print('构建 {} 的左腿'.format(self.__class__.__name__))


class Director:

	def build_person(self, pb):
		"""
		:type pb: PersonBuilder
		"""
		pb.build_head()
		pb.build_body()
		pb.build_right_arm()
		pb.build_left_arm()
		pb.build_right_leg()
		pb.build_left_leg()


if __name__ == '__main__':
	director = Director()
	fat_person = FatPerson()
	lean_person = LeanPerson()
	director.build_person(fat_person)
	director.build_person(lean_person)

# 其实director指挥者类可以省略掉, builder构建者基类里面可以创建构建流程的方法
# 模板方法模式, 也是定义了算法的骨架, 然后参数的获取通过函数让子类进行更改
# 建造者模式是 算法的骨架都是通过方法拼接暴露的

# 所以
# 模板方法模式 --算法骨架更抽象些-->建造者模式
# 建造者模式--建造过程更死一些-->模板方法模式

