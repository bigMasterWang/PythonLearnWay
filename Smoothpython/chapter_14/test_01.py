# -*- coding: utf-8 -*- 
# @Time     : 2021/5/9 17:55 
# @Author   : wangxiaofeng01@corp.netease.com
# @desc:    : 可迭代的对象, 迭代器和生成器

import re

RE_WORD = re.compile('\w+')

class Sentence(object):

	def __init__(self, text):
		self.text = text
		self.words = RE_WORD.findall(text)

	def __getitem__(self, item):
		return self.words[item]

	def __len__(self):
		return len(self.words)

s = Sentence('this is a sentence')
for item in s:
	print item
print s[0], s[1], s[2], s[3]

class GeneratorSentence(Sentence):

	def __iter__(self):
		for word in self.words:
			yield word
		return

s = GeneratorSentence('this is a generator')
for item in s:
	print item
print s[0], s[1], s[2], s[3]

# 生成器表达式
test = (x^2 for x in range(1, 10, 1))
for item in test:
	print item

# iter()的第二个参数, 就是返回这个哨符, 这是个标记值
# 意思是返回这个标记值时, 触发迭代器抛出StopIteration异常
import random
def d6():
	return random.randint(1, 30)

test = iter(d6, 1)
for x in test:
	print x,

# 把生成器当成协程, 注意, 虽然在协程中会使用yield产出值, 但这与迭代无关
# 所以本章只是讨论迭代技术的, 协程的特性之后再讲

# yield关键字只能把最近的外层函数变成生成器,如下
def f():
	x = 0
	while x < 10:
		x += 1
		yield x

def f2():
	def do_yield(n):
		yield n
	x = 0
	while x < 10:
		x += 1
		do_yield(x)
x = f()
y = f2()

print type(x)
print type(y)