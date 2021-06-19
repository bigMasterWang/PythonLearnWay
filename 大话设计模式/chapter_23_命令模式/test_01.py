# 第二十三章，烤羊肉串引来的思考——命令模式


# 命令模式： 讲一个请求封装为一个对象，从而使你可用不同的请求对客户进行参数化，对请求排队或记录请求日志
#           以及支持可撤销的操作

# 结构 client => command_controller -> command(abstract command) -> executor

from abc import ABC, abstractmethod


class CommandController(ABC):
	
	def set_command(self, _command):
		self.command = _command
	
	def execute_command(self):
		self.command.execute()


class BaseCommand(ABC):
	
	def __init__(self, _executor):
		self.executor = _executor
	
	@abstractmethod
	def execute(self):
		pass


class ConcreteCommand(BaseCommand):
	
	def execute(self):
		self.executor.action()


class Executor:
	
	def action(self):
		print(self.__class__.__name__, 'executive command!')



def test_01():
	et = Executor()
	c1 = ConcreteCommand(et)
	cc = CommandController()
	cc.set_command(c1)
	
	
	cc.execute_command()
	
	
# 总的来讲， 就是将客户端程序 和 程序执行者分开， 用一个command_controller作为控制
# 关键的是命令中需要包含执行者， 其实也可以将执行者放到command_controller中不是吗?, 这样才更合理
# 然后客户端只需要跟command_controller进行交流, 而不用知道是哪个executor执行的
"""就按照我们的想法写一下"""
class MyCommandController:
	
	def __init__(self, _executor):
		self.executor = _executor
		self.command = None
		
	def set_command(self, _command):
		self.command = _command
		
	def execute_command(self):
		"""
		可以在这个地方灵活实现, 到底是让command拿着executor, 还是让executor拿着command, 都可以
		站在程序的角度, 如果希望command自己内部执行log, 还是让command拿着executor比较好, 因为这样command毕竟然执行一个方法
		"""
		# self.executor.action(self.command)
		self.command.execute(self.executor)


class MyExecutor:
	
	def action(self, _command):
		print('executor: {} execute command :{}'.format(self.__class__.__name__, _command.__class__.__name__))


class MyCommand:
	
	
	def execute(self, executor):
		print('command log here and ')
		executor.action(self)
		


def test_02():
	my_et = MyExecutor()
	my_cc = MyCommandController(my_et)
	
	c1 = MyCommand()
	my_cc.set_command(c1)
	my_cc.execute_command()
	


if __name__ == '__main__':
	# test_01()
	test_02()