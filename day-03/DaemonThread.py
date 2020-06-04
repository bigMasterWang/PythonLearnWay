import threading


def thread_enter_function(max):
    iterator = range(0, max, 1).__iter__()
    try:
        while True:
            print(iterator.__next__())
    except StopIteration:
        print("线程执行完毕")


t1 = threading.Thread(target=thread_enter_function, args=(100,))
t1.setDaemon(True)
t1.start()

# there is no meaning to find out the difference of
# setDaemon(False) with join()

