# 简历复印——原型模式

# 原型模式：用原型实力指定创建对象的种类，并且通过拷贝这些原型对象创建新的对象
# 如果属性是引用类型，则复制引用但不复制引用的对象
# 如果属性是值类型，则对该字段进行逐位赋值


# 这里就不再进行引用类型的演示了
# 书上的做法也就是给引用的类型也加了一个clone的方法， 克隆的时候手动调用下

class Resume:
	
	def __init__(self):
		self.id = None
	
	def set_id(self, _id):
		self.id = _id
	
	def clone(self):
		class A:
			pass
		a = A()
		for k, v in self.__dict__.items():
			setattr(a, k, v)
		for k, v in self.__class__.__dict__.items():
			if k.startswith('__'):
				continue
			# 复制方法时必须这样，因为方法的属性是在类的__dict__中的
			setattr(a.__class__, k, getattr(self.__class__, k))
		return a


x = Resume()
x.set_id(1)
y = x.clone()
print(x.id)
print(y.id)

x.set_id(2)
y.set_id(3)
print(x.id)
print(y.id)

print(x.__dict__)
print(y.__dict__)
print(x.__class__.__dict__)
print(y.__class__.__dict__)
