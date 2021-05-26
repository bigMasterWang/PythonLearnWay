# -*- coding: utf-8 -*- 
# @Time     : 2021/5/9 17:06 
# @Author   : wangxiaofeng01@corp.netease.com
# @desc:    : 正确重载运算符
# 本章只讨论一元运算符和中缀运算符

# 不能重载内置类型的运算符
# 某些运算符不能重载, is and or not

# 1. 一元运算符
# -(__neg__) 一元取负运算符
# +(__pos__) 一元取正运算符
# ~(__invert__)对整数按位取反
import decimal
ctx = decimal.getcontext()

# 2. 增量运算符
# __iadd__, __imul__如果实现了__add__, __mul__那么增量运算符+=,*=不用编写额外的代码就能实现
# 如果实现了也会就地调用

