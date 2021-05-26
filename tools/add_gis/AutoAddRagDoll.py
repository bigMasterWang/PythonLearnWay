# -*- coding: utf-8 -*- 
# @Time     : 2021/3/8 19:08
# @Author   : wangxiaofeng01@corp.netease.com
# @desc:    : 自动添加gis动画
import xml.dom.minidom
import os
import copy

gim_files = []
physics_format_lines = []


def read_all_files():
	print 'start read target gim files'
	try:
		global gim_files
		with open('need_small_physics.csv') as lines:
			lines = lines.readlines()
			gim_files = [line[:-1] for line in lines]
		print 'read target gim files success !'
	except Exception as e:
		print e
		print 'read target gim files failed !'
		os.system('read files wrong')


def read_physics_format_lines():
	print 'start read physics format xml files'
	try:
		global physics_format_lines
		with open('physics_format.xml') as lines:
			physics_format_lines = lines.readlines()
		print 'read physics format xml files success !'
	except Exception as e:
		print e
		print 'read physics format xml files failed !'
		os.system('read format files wrong')


def add_physics_node(target_gim_file):
	print 'parse ', target_gim_file
	doc = xml.dom.minidom.parse(target_gim_file)
	expertise = doc.getElementsByTagName('Physics')
	if len(expertise) != 0:
		print target_gim_file, 'has already rag doll'
		return
	add_lines = parse_added_lines(doc)
	# 上面解析出来数据, 下面写入数据
	write_result(target_gim_file, add_lines)


def parse_added_lines(doc):
	# 解析出需要加入的lines
	neo_x_node = doc.firstChild
	# [0.0, 5.9852, -0.6871, 18.0638, 5.9852, 0.6871, 19.042]
	bounding_info = str(neo_x_node.getAttribute('BoundingInfo')).replace('(', '').replace(')', '')
	bounding_info = [float(item) for item in bounding_info.split(',')]
	# get the position and size in boundingInfo
	position = ','.join(str(item) for item in bounding_info[:3])
	size = ','.join(str(item) for item in bounding_info[3:6])
	add_lines = copy.deepcopy(physics_format_lines)
	add_lines[6] = add_lines[6].format(position)
	add_lines[9] = add_lines[9].format(size)
	return add_lines


def write_result(target_gim_file, result_physics_lines):
	print 'write ', target_gim_file
	with open(target_gim_file) as lines:
		sources_lines = lines.readlines()
	start = sources_lines[:-1]
	end = sources_lines[-1:]
	result_lines = start + result_physics_lines + end
	with open(target_gim_file, 'w') as f:
		f.writelines(result_lines)
	print target_gim_file, 'add rag doll success'


if __name__ == '__main__':
	read_all_files()
	read_physics_format_lines()
	for target_file in gim_files:
		if len(target_file) == 0:
			continue
		add_physics_node(target_file)
	print 'success !!!!!!!!!!'
	os.system('pause')
