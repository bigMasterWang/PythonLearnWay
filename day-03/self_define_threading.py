import threading
import time

class MyThread(threading.Thread):
    def __init__(self, max):
        super(MyThread,self).__init__()
        self.max = max

    @property
    def max(self):
        print("get function")
        return self._max

    @max.setter
    def max(self, value):
        print("set function")
        self._max = value

    def run(self):
        time.sleep(1)
        print("此线程是：",threading.current_thread().ident)
        print("赋值的变量是：",self.max)


t1 = MyThread(123)
t2 = MyThread(321)
t2.start()
t1.start()

