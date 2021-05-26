# -*- coding: utf-8 -*- 
# @Time     : 2020/8/24 15:40 
# @Author   : wangxiaofeng01@corp.netease.com
# @desc:    :

# 元组不仅仅是不可变列表
# 元组是对数据的记录，也就是说，因为不可变，其中信息的位置信息也很重要，嘚啵嘚、嘚啵嘚
# 举了个例子
traveler_ids = [('USA', '123456'), ("CHINA", '654321'), ("JAPAN", '123')]
for country, id in traveler_ids:
    print country

# 元组拆包， 就是TMD把元组里面不同的值分别做不同的处理（赋给不同的值）
# 也可以认为是“可迭代对象拆包”
# 方式一、平行赋值， _在国际化的软件中并不是一个很好的占位符，但其它情况下是很好的占位符
a, b = (1, 2)
print a, b
# 方式二、不使用中间变量交换两个变量的值
b, a = a, b
print a, b
# 方式三、使用* 将元组拆分, 使用**将字典拆分(字典的key必须是str，且和函数定义时的param名字一样，数量一样)
def test_func_1(a, b):
    return a / b, a % b
def test_fun_2(a=None, b=None):
    return a / b, a % b
def test_fun_3(x, y, a=None, b=None):
    return x / y, x % y, a / b, a % b


params_tuple = (20, 8)
params_dict = {'a': 20, 'b': 8}

print test_func_1(*params_tuple)

print test_fun_2(**params_dict)

print test_fun_3(*params_tuple, **params_dict)

# 方式四， 使用*来获取其他不想要的信息
# a, b, *reset = range(5), 但是在python2中不能使用， python3中可以
a = range(5)
a, b, c, d, e = a
print a, b, c, d, e



# 嵌套元组拆包
metro_areas = [
    ('王晓峰', '男', 23, ('河南省', '项城市', '惠民小区')),
    ('张冠举', '男', 24, ('河南省', '项城市', '袁张营')),
    ('龙斌', '男', 24, ('河南省', '项城市', '荣楼'))
]
for name, sex, age, (province, area, city) in metro_areas:
    print name, province

# 总结下来，就两种，一种是平行赋值，另一种是*和**的用法