# -*- coding: utf-8 -*- 
# @Time     : 2020/8/18 15:30 
# @Author   : wangxiaofeng01@corp.netease.com
# @desc:    : 这个文件是测试twisted的类
from twisted.internet import reactor, protocol, task, defer
from twisted.internet.protocol import connectionDone
from twisted.internet.task import Clock, deferLater
import time
# 继承protocol.Protocol
# 并重写其中的几个重要方法
class Echo(protocol.Protocol):
    """This is just about the simple possible protocol
    """

    def dataReceived(self, data):
        # 接收到数据，立即返回
        # self.transport.write(data)
        print data

    def connectionMade(self):
        # 接收到连接请求
        pass

    def connectionLost(self, reason=connectionDone):
        # 断开连接
        print '客户端断开连接'

def main():
    """this runs the protocol on port 8000"""
    factory = protocol.Factory()
    factory.protocol = Echo
    # 监听的端口是估计是0.0.0.0，所以不用设置特定的ip

    server_time_loop = task.LoopingCall(time_task)
    server_time_loop.start(1)

    add_func(4, say_hello)

    reactor.listenTCP(8000, factory)
    reactor.run()


def time_task_two():
    print '这里是2'

def time_task():
    print '被调用了'

def add_func(time, func):
    reactor.callLater(time, func)



def say_hello():
    print 'hello'



if __name__ == '__main__':
    main()


