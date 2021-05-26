# -*- coding: utf-8 -*- 
# @Time     : 2021/5/12 22:40 
# @Author   : wangxiaofeng01@corp.netease.com
# @desc:    :

import os
import time
import sys

import requests

POP20_CC = ('CN IN US ID BR PK NG').split()

BASE_URL = 'http://flupy.org/data/flags'

DEST_DIR = os.path.join(os.path.dirname(os.path.abspath('test_01.py')), 'down_loads')


def save_flag(img, filename):
	path = os.path.join(DEST_DIR, filename)
	with open(path, 'wb') as fp:
		fp.write(img)


def get_flag(cc):
	url = '{}/{cc}/{cc}.gif'.format(BASE_URL, cc=cc.lower())
	resp = requests.get(url)
	return resp.content


def show(text):
	print(text, end=' ')
	sys.stdout.flush()


def download_many(cc_list):
	for cc in sorted(cc_list):
		image = get_flag(cc)
		show(cc)
		save_flag(image, cc.lower() + '.gif')


def main(download_many):
	to = time.time()
	count = download_many(POP20_CC)
	elapsed = time.time() - to
	msg = '\n{} flags downloaded in {:2f}s'
	print(msg.format(count, elapsed))


if __name__ == '__main__':
	main(download_many)
