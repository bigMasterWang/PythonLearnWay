import threading

# 一定要用这个类创造一个红绿灯
# 或者说用coroutine什么的，一定要实现一个完美的红绿灯
my_event = threading.Event()
print_lock = threading.Lock()


def traffic_light():
    global my_event
    my_event.set()
    while True:
        my_event.set()
        x = input("please set the traffic light status\n")
        if x == "green":
            my_event.set()
        if x == "red":
            my_event.clear()


def cars():
    global my_event
    while True:
        if my_event.isSet():
            print("车辆:", threading.current_thread().ident, "通过了")
        else:
            print("车辆:", threading.current_thread().ident, "等待")
        my_event.clear()
        my_event.wait()


light_thread = threading.Thread(target=traffic_light)
light_thread.start()
my_cars_list = [threading.Thread(target=cars)
                for _ in range(1)]
for td in my_cars_list:
    td.start()

# 总结就是 set(),clear(),wait()方法
# wait()只有在flag=True的时候才会被唤醒
