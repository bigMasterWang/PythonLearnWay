import threading
import time

MAX_CONNECTIONS = 5

def thread_work_function(semaphore):
    semaphore.acquire()
    print("当前线程名称：",threading.current_thread().ident)
    time.sleep(1)
    semaphore.release()



if __name__ == "__main__":
        semaphore = threading.BoundedSemaphore(MAX_CONNECTIONS)
        threads = [threading.Thread(target=thread_work_function,
                                    args=(semaphore,))
                   for _ in range(10)]
        for it in threads:
            it.start()
            # 不能jion哈，这样就没法证明都进去了
            # 也就是说在争抢semaphore的时候，是在主线程中进行的
