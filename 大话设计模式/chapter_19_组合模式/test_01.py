# -*- coding: utf-8 -*-
# @Time     : 2021/6/15 12:22
# @Author   : wangxiaofeng01@corp.netease.com
# @desc:    : 第十九章 分公司=一部门——组合模式

# 组合模式: 将对象组合成树形结构以表示'部分-整体'的层次结构.组合模式使得用户对单个对象和组合对象的使用具有一致性.

# 结构如下
from abc import ABC, abstractmethod


class Component(ABC):

	def __init__(self, name):
		self.name = name
		self.children = set()

	@abstractmethod
	def add(self, _component):
		pass

	@abstractmethod
	def remove(self, _component):
		pass

	@abstractmethod
	def display(self, dep):
		pass


class Composite(Component):
	def add(self, _component):
		self.children.add(_component)

	def remove(self, _component):
		self.children.add(_component)

	def display(self, dep):
		print('\t' * dep, self.name)
		for com in self.children:
			com.display(dep + 1)


class Leaf(Component):
	def add(self, _component):
		print('leaf can not add')

	def remove(self, _component):
		print('leaf can not remove')

	def display(self, dep):
		print('\t' * dep, self.name)


def test_01():
	root = Composite('root')
	root.add(Leaf('Leaf A'))
	root.add(Leaf('Leaf B'))

	comp1 = Composite('Composite X')
	comp1.add(Leaf('Leaf XA'))
	comp1.add(Leaf('Leaf XB'))
	root.add(comp1)

	comp2 = Composite('Composite Y')
	comp2.add(Leaf('Leaf YA'))
	comp2.add(Leaf('Leaf YB'))
	comp1.add(comp2)

	root.display(1)


# 透明方式和安全方式
# 透明方式: 所有的节点都继承同一个父节点, 接口都一样, 但是有些节点的一些接口是没有实现的, 所以不安全
# 安全方式: 枝节点管理add和remove, 叶子节点不具备, 这样就安全, 但是使用有区别, 就不透明了

# 何时使用组合模式
# 需求中是体现部分与整体层次的结构时, 以及你希望用户可以忽略组合对象与单个对象的不同, 统一地使用组合结构中地所有对象时, 考虑使用组合模式


# 公司管理系统
# 公司: 子公司, 各种部门
# 财务部: 履行职责
# 人力资源部: 履行职责
# 子公司: 子公司, 各种部门, 办事处
# 办事处: 各种部门


class Company(ABC):
	def __init__(self, name):
		self.children = set()
		self.name = name

	@abstractmethod
	def add_company(self, _company):
		pass

	@abstractmethod
	def remove_company(self, _company):
		pass

	@abstractmethod
	def display(self, dep):
		pass

	@abstractmethod
	def work(self):
		pass


class ConcreteCompany(Company):

	def add_company(self, _company):
		self.children.add(_company)

	def remove_company(self, _company):
		self.children.remove(_company)

	def display(self, dep):
		print('\t'*dep, self.name)
		for com in self.children:
			com.display(dep+1)

	def work(self):
		for com in self.children:
			com.work()


class HRDepartment(Company):

	def add_company(self, _company):
		pass

	def remove_company(self, _company):
		pass

	def display(self, dep):
		print('\t'*dep, self.name)

	def work(self):
		print(self.name, 'HR部门负责招聘员工')


class FinanceDepartment(Company):

	def add_company(self, _company):
		pass

	def remove_company(self, _company):
		pass

	def display(self, dep):
		print('\t'*dep, self.name)

	def work(self):
		print(self.name, '财务部门负责财务管理')


def test_02():
	root = ConcreteCompany('总公司')
	root.add_company(HRDepartment('总公司hr部门'))
	root.add_company(FinanceDepartment('总公司财务部门'))

	comp1 = ConcreteCompany('华东区分公司')
	comp1.add_company(HRDepartment('华东分司hr部门'))
	comp1.add_company(FinanceDepartment('华东分司财务部门'))
	root.add_company(comp1)

	comp2 = ConcreteCompany('南京办事处')
	comp2.add_company(HRDepartment('南京办事处hr部门'))
	comp2.add_company(FinanceDepartment('南京办事处财务部'))
	comp1.add_company(comp2)

	comp3 = ConcreteCompany('杭州办事处')
	comp3.add_company(HRDepartment('杭州办事处hr部门'))
	comp3.add_company(FinanceDepartment('杭州办事处财务部'))
	comp1.add_company(comp3)

	# root.work()
	root.display(1)


if __name__ == '__main__':
	# test_01()
	test_02()

