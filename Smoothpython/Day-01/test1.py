# coding=utf-8
import collections

# 构建一个对象(只有属性，没有方法)，但是不能改变属性
Card = collections.namedtuple('Card', ['rank', 'suit'])
c = Card(1, 2)
print c.suit
# print c

suit = 'a b c d'
# print suit.split()
sorted()

class Friends(object):

    def __init__(self):
        self.friends = [1, 2, 3, 4, 5, 6]
        self.index = 0

    # def __len__(self):
    #     return len(self.friends)
    #
    # def __getitem__(self, position):
    #     return self.friends[position]

    def __iter__(self):
        return self.friends.__iter__()

    def next(self):
        # return next(self.friends)
        while True:
            if self.index >= len(self.friends):
                raise StopIteration
            else:
                save = self.index
                self.index += 1
                return self.friends[save]


a = Friends()
for item in a:
    print item,
print a[0]
# 这个调用的就是 __getitem__()
# print a[0]
# 这个调用的就是 __len__()
# rint len(a)
# print sorted(a, key=lambda x: -x)
# 支持切片
# print a[1:]

# 这个调用的时

#  for loop 应该是先去找__len__()和__getitem__()
# for i in a:
#     print i,


# import random
# print a[random.randint(0, len(a)-1)]
#
#
# test = collections.namedtuple('TestOject',['name', 'value'])
# a = [test('1', '1'), test('2', '2'), test('3', '3'), test('4', '4')]
# # 按照value降序
# print sorted(a, key=lambda x: x[1], reverse=True)
# # 按value升序
# print sorted(a, cmp=lambda x, y: x[1] > y[1])





