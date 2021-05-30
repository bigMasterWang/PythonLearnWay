# 考题抄错会做也白搭——模板方法模式


# 模板方法模式: 定义一个操作中的算法的骨架,而将一些步骤延迟到子类中.
# 模板方法使得子类可以不改变一个算法的结构即可重定义该算法的某些特定步骤
# (就是骨架方法中使用其他的方法来获取参数, 子类只用重写获取方法的参数即可)


# 当我们要完成在某一细节层次一致的一个过程或一系列步骤,但其个别步骤在更详细的层次
# 上的实现可能不同时, 我们通常考虑用模板方法模式来处理
from abc import ABC, abstractmethod


class TestPaper(ABC):
	
	def __init__(self):
		self.name = None
	
	def test_one(self):
		print('第一题: 龙斌是傻逼吗? A:是 B:不是')
		print('{}\t选择\t{}'.format(self.name, self.answer_a()))
	
	def test_two(self):
		print('第一题: 龙斌不是傻逼? A:不对 B:对')
		print('{}\t选择\t{}'.format(self.name, self.answer_b()))
	
	@abstractmethod
	def answer_a(self):
		return ''
	
	@abstractmethod
	def answer_b(self):
		return ''


class William(TestPaper):
	
	def __init__(self):
		super().__init__()
		self.name = 'William'
	
	def answer_a(self):
		return 'A'
	
	def answer_b(self):
		return 'A'


class LongBin(TestPaper):
	
	def __init__(self):
		super().__init__()
		self.name = '龙斌'
	
	def answer_a(self):
		return 'B'
	
	def answer_b(self):
		return 'B'


if __name__ == '__main__':
	w = William()
	l = LongBin()
	print('==========================================')
	w.test_one()
	w.test_two()
	print('==========================================')
	l.test_one()
	l.test_two()

# 模板方法模式是通过把不变的行为搬到超类, 去除子类中重复的代码来体现他的优势
