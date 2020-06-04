# 生产者与消费者
import threading
import time

cargo = 100
condition_lock = threading.Condition()

finished_producer = 0
finished_consumer = 0
finished_lock = threading.Lock()


def producer_enter_function():
    my_money = 0
    global cargo
    global condition_lock
    global finished_producer
    global finished_consumer
    global finished_lock
    while True:
        if my_money >= 1000 or finished_consumer == 10:
            print("producer：", threading.current_thread().ident, "get enough money：", my_money)
            finished_lock.acquire()
            finished_producer += 1
            finished_lock.release()
            break
        condition_lock.acquire()
        if cargo <= 100:
            cargo += 100
            my_money += 100

        # why the sleep() must after release()
        # if I change their position, program goes wrong
        # why?
        condition_lock.release()
        time.sleep(0.01)


def consumer_enter_function():
    my_cargo = 0
    global condition_lock
    global cargo
    global finished_consumer
    global finished_lock
    while True:
        if my_cargo >= 1000:
            print("consumer ：", threading.current_thread().ident, "get enough cargo ：", my_cargo)
            finished_lock.acquire()
            finished_consumer += 1
            finished_lock.release()
            break
        condition_lock.acquire()
        if cargo > 100:
            cargo -= 100
            my_cargo += 100
        condition_lock.release()
        time.sleep(0.01)


producers = [threading.Thread(target=producer_enter_function)
             for _ in range(10)]
for item in producers:
    item.start()

consumers = [threading.Thread(target=consumer_enter_function)
             for _ in range(10)]
for item in consumers:
    item.start()

while True:
    print(cargo)
    print("the finished consumer number:", finished_consumer)
    print("the finished producer number:", finished_producer)
    if finished_consumer == 10 and finished_producer == 10:
        break
    time.sleep(1)
