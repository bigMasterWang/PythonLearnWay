# -*- coding: utf-8 -*- 
# @Time     : 2020/8/13 16:24 
# @Author   : wangxiaofeng01@corp.netease.com
# @desc:    : 得到文件夹所有的py文件路径

# import glob, os
# os.chdir("TestModule")
# for file in glob.glob("*.py"):
#     print(file)


import os

all_modules_path = []

# root就是你输入的目录，作为根目录
# dirs就是当前目录下的目录列表
# files就是当前遍历的目录下所有的文件
for root, dirs, files in os.walk(""):
    for file in files:
        if file.endswith(".py") and file != '__init__.py':
            all_modules_path.append(root + '/' +file)
            # print os.path.join(root, file)


for item in all_modules_path:
    print item

