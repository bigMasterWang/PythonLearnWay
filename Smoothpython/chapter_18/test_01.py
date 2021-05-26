# -*- coding: utf-8 -*-
# @Time     : 2021/5/17 20:59
# @Author   : wangxiaofeng01@corp.netease.com
# @desc:    : 使用asyncio包处理并发

# 反正也只是python3的, 看看就完了

# 并发是指一次处理多件事
# 并行是指一次做多件事
# 二者不同, 但是有联系
# 一个关于结构, 一个关于执行
# 并发用于指定方案, 用来解决可能(但未必)并行的问题

import threading
import itertools
import time
import sys

# 使用线程

class Signal:
	# 从外部控制线程
	go = True


def spin(msg, signal):
	write, flush = sys.stdout.write, sys.stdout.flush
	for char in itertools.cycle('|/-\\'):
		status = char + ' ' + msg
		write(status)
		flush()
		write('\x08' * len(status))
		time.sleep(.1)
		if not signal.go:
			break
	write(' ' * len(status) + '\x08' * len(status))


def slow_function():
	time.sleep(3)
	return 42


def supervisor():
	signal = Signal()
	spinner = threading.Thread(target=spin, args=('thinking!', signal))
	spinner.start()
	res = slow_function()
	signal.go = False
	# spinner.join()
	return res


if __name__ == '__main__':
	result = supervisor()
	print('Answer: ', result)
