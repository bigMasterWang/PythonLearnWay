# -*- coding: utf-8 -*- 
# @Time     : 2021/5/13 0:15 
# @Author   : wangxiaofeng01@corp.netease.com
# @desc:    :
import time

import requests
import os
import sys

POP20_CC = ('CN IN US ID BR PK NG AD AE AF AG AL').split()

BASE_URL = 'http://flupy.org/data/flags'

DEST_DIR = os.path.join(os.path.dirname(os.path.abspath('test_02.py')), 'down_loads')


def get_flag(cc):
	url = '{}/{cc}/{cc}.gif'.format(BASE_URL, cc=cc.lower())
	image = requests.get(url)
	return image.content


def show(text):
	print(text, end=' ')
	sys.stdout.flush()

def download_many(cc_list, saver):
	for cc in cc_list:
		image = get_flag(cc)
		show(cc)
		# 最起码写入的时候不耽误继续下载
		saver.send((image, cc+'.gif'))
	return len(cc_list)

def main(download_many):
	t0 = time.time()
	saver = yield_save_image()
	next(saver)
	download_many(POP20_CC, saver)
	print(time.time() - t0)

# 通过写上面的coroutine, 还是感觉到coroutine用于自循环的一个独立系统, 外界通过send()
# 传递参数, 对该系统产生影响

from concurrent import futures
MAX_WORKERS = 20

def yield_save_image():
	while True:
		data = yield
		image, filename = data[0], data[1]
		print('coroutine received :', filename)
		path = os.path.join(DEST_DIR, filename)
		with open(path, 'wb') as fp:
			fp.write(image)

def save_flag(image, name):
	path = os.path.join(DEST_DIR, name)
	with open(path, 'wb') as fp:
		fp.write(image)

# 使用concurrent.futures模块下载
# 多线程最好还是不要用coroutine, 因为coroutine多线程不安全
def download_one(cc, saver):
	print(saver.__name__)
	image = get_flag(cc)
	show(cc)
	saver.send((image, cc.lower()+'.gif'))

def download_many_by_threads(cc_list):
	savers = [yield_save_image() for i in range(0, len(cc_list))]
	[next(x) for x in savers]
	print(savers)
	workers = min(MAX_WORKERS, len(cc_list))
	with futures.ThreadPoolExecutor(workers) as executor:
		res = executor.map(download_one, sorted(cc_list), savers)
	return len(list(res))


if __name__ == '__main__':
	# main(download_many)
	t0 = time.time()
	count = download_many_by_threads(POP20_CC)
	elapsed = time.time()
	print('{} spend {} s'.format(count, elapsed-t0))