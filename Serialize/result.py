# -*- coding: utf-8 -*- 
# @Time     : 2020/8/13 17:10 
# @Author   : wangxiaofeng01@corp.netease.com
# @desc:    : 拿到一个文件夹下所有文件中的所有类


import os
import imp
import inspect


def get_all_class_from_modules(modules_list):
    """可以用inspect直接根据module拿到其中所有的类 wangxiaofeng01@corp.netease.com

    :param modules_list:
    :return:
    """
    class_list = {}
    for module in modules_list:
        for name, obj in inspect.getmembers(module, inspect.isclass):
                class_list[name] = obj
    return class_list



def get_all_modules(modules_path_list):
    """ 根据文件的路径，可以通过imp直接引入这个文件module wangxiaofeng01@corp.netease.com

    :param modules_path_list:
    :return:
    """
    all_modules = []
    for path in modules_path_list:
        module = imp.load_source('', path)
        all_modules.append(module)
    return all_modules


def get_all_modules_path(dir):
    """../代表上层路径开始，直接写相当于当前路径开始 wangxiaofeng01@corp.netease.com
    用os.walk可以递归找到所有的文件

    :param dir: the modules you need dir
    :return: list[modules]
    """
    all_modules_path = []
    # root就是你输入的目录，作为根目录
    # dirs就是当前目录下的目录列表
    # files就是当前遍历的目录下所有的文件
    for root, dirs, files in os.walk(dir):
        for file in files:
            if file.endswith(".py") and file != '__init__.py':
                all_modules_path.append(root + '/' + file)
    return all_modules_path


class_dict = get_all_class_from_modules(get_all_modules(get_all_modules_path('../Serialize/TestModule')))
for item in class_dict.iteritems():
    print item[0], item[1]

# 结合protobuff的序列化，就可以比较完美的解决网络消息传递的问题了
