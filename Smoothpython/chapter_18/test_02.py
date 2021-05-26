# -*- coding: utf-8 -*- 
# @Time     : 2021/5/18 19:35 
# @Author   : wangxiaofeng01@corp.netease.com
# @desc:    :

# 使用asyncio包的协程
import asyncio
import itertools
import sys

# 有关python3的并发, 并行, 异步问题就此为止,
# 之后如果用到python3再进行研究

# @asyncio.coroutine
# def spin(msg):
# 	write, flush = sys.stdout.write, sys.stdout.flush
# 	for char in itertools.cycle('|/-\\'):
# 		status = char + ' ' + msg
# 		write(status)
# 		flush()
# 		write('\x08' * len(status))
# 		try:
# 			yield from asyncio.sleep(.1)
# 		except asyncio.CancelledError:
# 			break
# 	write(' ' * len(status) + '\x08' * len(status))