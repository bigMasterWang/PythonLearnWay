# -*- coding: utf-8 -*- 
# @Time     : 2020/8/18 16:11 
# @Author   : wangxiaofeng01@corp.netease.com
# @desc:    : 测试客户端

import socket


client = socket.socket()
client.connect(("127.0.0.1", 8000))

client.send("hello world")