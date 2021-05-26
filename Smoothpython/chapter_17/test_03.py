# -*- coding: utf-8 -*- 
# @Time     : 2021/5/13 21:03 
# @Author   : wangxiaofeng01@corp.netease.com
# @desc:    :

# 期物在哪里
import time
import random
from concurrent import futures


def sleep_print():
	sleep_time = random.randint(1, 10)
	time.sleep(sleep_time)
	print('I am wake')
	return sleep_time


def main():
	cc_list = ['one', 'two', 'three', 'four', 'five']
	with futures.ThreadPoolExecutor(max_workers=5) as executor:
		to_do = []
		for i in range(0, 5, 1):
			# 返回一个期物
			future = executor.submit(sleep_print)
			to_do.append(future)
			print('Scheduled for {}: {}'.format(cc_list[i], future))
		for future in futures.as_completed(to_do):
			res = future.result()
			print('{} result: {}'.format(future, res))


if __name__ == '__main__':
	pass
# main()


# GIL(global interpreter lock) 全局解释器锁
# 既然python线程受GIL的限制, 任何时候都只允许运行一个线程, 那么flags_threadpool.py脚本
#		为什么会比flags.py快5倍?
# flags_asyncio.py脚本和flags.py脚本都在单个线程中运行, 前者怎么会比后者快5倍?

# 阻塞型i/o和GIL
# 编写python代码时无法控制GIL, 其实, 有一个使用c语言编写的python库能管理GIL, 自行
# 启动操作系统线程, 利用全部可用的cpu核心.
# 然而标准库中所有执行阻塞型i/o操作的函数, 在等待操作系统返回结果时都会释放GIL.
# 这意味着Python语言这个层次上可以使用多线程, 而I/O密集型程序能从中受益
# 一个python线程等待网络响应时, 阻塞型i/o函数会释放GIL, 在运行一个线程

# cpu密集型使用进程池, i/o密集型使用线程池(反正进程池也得不到任何好处)

# 使用concurrent.futures模块启动进程(processpool)
# 如果需要cpu密集型, 此模块能绕开GIL, 利用所有可利用的cpu核心

def logger(n):
	print('I am sleep for: {}s'.format(n))
	time.sleep(n)
	print('I am wake')
	return n


executor = futures.ThreadPoolExecutor(max_workers=3)
# 返回的只是一个生成器, 需要拿结果时自然会阻塞, 这也是一个特性, 后面的结果会被阻塞
# 而executor.submit和futures.as_completed就能解决这个问题
results = executor.map(logger, range(5))
for index, result in enumerate(results):
	print('result[{}]: {}'.format(index, result))


