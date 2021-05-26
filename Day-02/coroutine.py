# coding=utf-8
# corountine


#  as only after calling __next__() method, out coroutine starts executing.
#  After this call, execution advances to the first yield expression,
#  now execution pauses and wait for value to be sent to corou object.
#  When first value is sent to it, it checks for prefix and print name if prefix present.
#  After printing name it goes through loop until it encounters name = (yield) expression again.
# def print_name(prefix):
#     print("Searching prefix:{}".format(prefix))
#     while True:
#         name = (yield)
#         if prefix in name:
#             print(name)
#
#
# my_iterator = print_name("Dear")
# # why should execute __next__ first?
# my_iterator.__next__()
# my_iterator.send("zgj")
# my_iterator.send("Dear william")
#
#
# def print_name_two(prefix):
#     print("Searching prefix:{}".format(prefix))
#     try:
#         while True:
#             name = (yield)
#             if (prefix in name):
#                 print(name)
#     except GeneratorExit:
#         print("Closing coroutine!")
#
#
# my_iterator_two = print_name_two("Dear")
# my_iterator_two.__next__()
# my_iterator_two.send("ls")
# my_iterator_two.send("Dear William")
# my_iterator_two.close()


# 自己想一个很有意思的例子 corountine chaining
# 选择飞行员，条件：
# physique:good
# nervous_system:good
# eyesight:good
# 数据格式[{"physique":"","nervous_system":"","eyesight":""},{}]

# 开始是一个正常的函数
def filter_fighter_pilots(candidate_list, next_coruntine):
    for item in candidate_list:
        next_coruntine.send(item)
    next_coruntine.close()


def filter_physique(next_corountine):
    try:
        while True:
            candidate = (yield)
            if (candidate["physique"] == "good"):
                next_corountine.send(candidate)
    except GeneratorExit:
        print("physique filter is done")


def filter_nervous_system(next_coroutine):
    try:
        while True:
            candidate = (yield)
            if (candidate["nervous_system"] == "good"):
                next_coroutine.send(candidate)
    except GeneratorExit:
        print("nervous system filter is done")


def filter_eyesight():
    try:
        while True:
            candidate = (yield)
            if (candidate["eyesight"] == "good"):
                print(candidate)
    except GeneratorExit:
        print("eyesight filter is done")


candidate_list = [{"physique": "good", "nervous_system": "good", "eyesight": "good", "name": "王晓峰"},
                  {"physique": "medium", "nervous_system": "good", "eyesight": "good", "name": "张冠举"},
                  {"physique": "bad", "nervous_system": "good", "eyesight": "good", "name": "李森"},
                  {"physique": "good", "nervous_system": "good", "eyesight": "good", "name": "李金泽"},
                  {"physique": "good", "nervous_system": "good", "eyesight": "good", "name": "肖杨杨"},
                  {"physique": "medium", "nervous_system": "good", "eyesight": "good", "name": "马原振"},
                  {"physique": "bad", "nervous_system": "good", "eyesight": "good", "name": "种旭萍"}, ]

filter_eyesight_iterator = filter_eyesight()
filter_eyesight_iterator.__next__()
filter_nervous_system_iterator = filter_nervous_system(filter_eyesight_iterator)
filter_nervous_system_iterator.__next__()
filter_physique_iterator = filter_physique(filter_nervous_system_iterator)
filter_physique_iterator.__next__()

filter_fighter_pilots(candidate_list, filter_physique_iterator)


# Threads require a lot of memory, about 8MB per executing thread.
# coroutine is implemented as an extension to generators.
# The cost of starting a generator coroutine is a function call.
# Once active, they each use less than 1KB of memory until they’re exhausted.

# 这样写有任何用吗？？



