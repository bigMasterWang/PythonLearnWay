# -*- coding: utf-8 -*- 
# @Time     : 2020/9/15 14:17 
# @Author   : wangxiaofeng01@corp.netease.com
# @desc:    :

# select.select(rlist, wlist, xlist[, timeout])
# This is a straightforward interface to the Unix select() system call.
# The first three arguments are sequences of ‘waitable objects’:
# either integers representing file descriptors or
# objects with a parameterless method named fileno() returning such an integer:

import socket
import select

read_list = []
write_list = []


class TestClient(object):

    def __init__(self, client_socket):
        super(TestClient, self).__init__()
        self.client_socket = client_socket
        global read_list, write_list
        read_list.append(self)
        write_list.append(self)

    def fileno(self):
        return self.client_socket.fileno()

    def read(self):
        data = self.client_socket.recv(1024)
        if data == '':
            read_list.remove(self)
            write_list.remove(self)
            self.client_socket.close()
            print '客户端关闭'
            return
        print '收到客户端客户端:', self.client_socket, ' 的消息', data
        self.client_socket.send('我收到你的消息了')

    def write(self):
        # client.sendall('welcome to server')
        # client.close()
        pass


class TestServer(object):

    def __init__(self):
        super(TestServer, self).__init__()
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind(('0.0.0.0', 12345))
        self.server.listen(5)

    def fileno(self):
        return self.server.fileno()

    def read(self):
        client, addr = self.server.accept()
        print '连接了新的客户端'
        TestClient(client_socket=client)

    def write(self):
        pass


server = TestServer()
read_list.append(server)

while True:
    read_able, write_able, _ = select.select(read_list, write_list, [])
    for r in read_able:
        r.read()
    for w in write_list:
        w.write()


# 网络数据库的一种实现思路
# 1. 调用网络数据库接口后:
#  1.1 在主循环中暂停
#  1.2 并设置该接口的等待标志,并在此函数中执行main loop
#  1.3 接收到返回的结果后(用全局的实例接受结果),ruturn参数,break,然后让main loop 继续执行




