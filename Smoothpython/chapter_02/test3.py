# -*- coding: utf-8 -*- 
# @Time     : 2020/8/24 17:53 
# @Author   : wangxiaofeng01@corp.netease.com
# @desc:    : 切片

# 切片切的是index [x:y]  x<=index<y
a = [1, 2, 3, 4, 5, 6, 7]
print a[0:len(a)]
print a[2:len(a)]
print a[:2]


# 间隔切片
s = 'bicycle'
print s[::3]
print s[::-1]
print s[::-2]

# 高级切片 iteration[a:b:c] 在a, b之间以c为间隔切片， c负值意味着反向
test = range(1, 11)
print test
# 这个当c为负值的时候,还需要仔细研究
print test[5:len(test):1]

print 'flag flag'
# 这样先把切片的切法slice定义出来，取上名字，之后再进行切片的时候就很简单了
slice_1 = slice(1, 12, 2)
print test[slice_1]


print '切片变量'
# 给切片赋值
l = range(10)
l[2:5] = [20, 30]
print l
del l[5: 7]
print l

# 这一句话就必须替换的数量和后面数组中元素的数量一致了
l[3:: 2] = [11, 22]
print l

# 总结一下就是入宫赋值的对象是一个切片，那么赋值语句的右侧必须是一个可迭代对象， 即使只有一个值，也要转化为可迭代的序列
# 如下， 立即报错 “TypeError: can only assign an iterable”
# l[1: 3] = 100
# print l
