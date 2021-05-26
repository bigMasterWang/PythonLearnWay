# -*- coding: utf-8 -*- 
# @Time     : 2020/12/8 16:23 
# @Author   : wangxiaofeng01@corp.netease.com
# @desc:    : 将场景中的物体转化为参与交互的


import os

print u'输入文件全路径名: '
file_path = raw_input()
lines = []


def read_scene():
    try:
        with open(file_path, 'r') as f:
            global lines
            lines = f.readlines()
    except Exception as e:
        print e
        os.system("pause")
    print u'读取完毕'


def process_lines():
    global lines
    for i in range(0, len(lines)):
        if 'Flag="6146"' in lines[i]:
            lines[i] = lines[i].replace('Flag=\"6146\"', 'Flag=\"6162\"')
        if 'Flag="8394754"' in lines[i]:
            lines[i] = lines[i].replace('Flag=\"8394754\"', 'Flag=\"8394770\"')
    print u'处理完毕'


def write_scene():
    try:
        with open(file_path, 'w') as f:
            global lines
            f.writelines(lines)
    except Exception as e:
        print e
        os.system("pause")
    print u'更改完毕'



if __name__ == '__main__':
    read_scene()
    process_lines()
    write_scene()
    os.system("pause")