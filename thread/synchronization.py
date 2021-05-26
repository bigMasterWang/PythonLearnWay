import threading
import time

x = 0


def increment():
    global x
    x += 1


def thread_task(lock):
    for _ in range(100000):
        lock.acquire()
        increment()
        lock.release()


def main_task():
    global x
    x = 0

    lock = threading.Lock()

    t1 = threading.Thread(target=thread_task, args=(lock,))
    t2 = threading.Thread(target=thread_task, args=(lock,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()


if __name__ == "__main__":
    for i in range(0, 10, 1):
        start_time = time.process_time()
        main_task()
        end_time = time.process_time()
        print("Itreation {}:x = {} 时间经过{}".format(i, x, end_time - start_time))
