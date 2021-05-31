# 事件委托实现, C#有delegate的委托机制
# python模仿C#的delegate实现下委托
class DelegateTask:
	
	def __init__(self, cb, *args, **kwargs):
		self.cb = cb
		self.args = args
		self.kwargs = kwargs
	
	def execute(self):
		self.cb(*self.args, **self.kwargs)


# 这个委托比C#的更灵活, 不限制参数类型和个数
class Delegate:
	def __init__(self):
		self._cbs = []
	
	def __iadd__(self, other):
		self._cbs.append(DelegateTask(*other))
		return self
	
	def notify(self):
		for cb in self._cbs:
			cb.execute()


class Secretary:
	
	def __init__(self, delegate):
		self.delegate = delegate
	
	def notify(self):
		self.delegate.notify()


class LookNBAColleagues:
	
	def __init__(self, name):
		self.name = name
	
	def stop_look_nba(self, why):
		print('{} stop look nba because {}'.format(self.name, why))


class PlayGameColleagues:
	
	def __init__(self, name):
		self.name = name
	
	def stop_play_games(self, if_not_str):
		print('{} stop play game if not, {}'.format(self.name, if_not_str))


if __name__ == '__main__':
	d = Delegate()
	secretary = Secretary(d)
	colleagues_a = LookNBAColleagues('张冠举')
	colleagues_b = PlayGameColleagues('龙斌')
	secretary.delegate += (colleagues_a.stop_look_nba, ' 你老板胡汉三又回来了!')
	secretary.delegate += (colleagues_b.stop_play_games, ' 你老板胡汉三会扣你的工资!')
	secretary.notify()

# 其实python这种观察者模式天然写起来就简单, 因为函数也是对象嘛, 可以直接当参数传递
# !!!!如果不是为了模仿C#的delegate的委托机制, 直接在secretary里面直接搞一个cb的数组即可, 根本不需要_delegate的类在中间搞一层
# 甚至重写secretary的__iadd__(self,other)都会更加简单


# !但是确实这样搞把观察者和通知者完全解耦了, 他们之间相互不知道任何信息
# 关键就在于事件的注册放到了客户端程序里面, 并且注册的是回调函数, 这样通知者就不用知道通知者是谁了!!!!!!
