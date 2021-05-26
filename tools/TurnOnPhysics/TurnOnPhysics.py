# -*- coding: utf-8 -*- 
# @Time     : 2021/3/19 9:52 
# @Author   : wangxiaofeng01@corp.netease.com
# @desc:    : this is for auto turn on physics in .scn file

import xml.dom.minidom
import os

physics_gim_files = set()

physics_data = {
	'Flag': '4106',
	'ModelFlag': '8'
}


# 1. 读取所有模型
# 2. 分析scn文件
# 3. 找到这些模型, 然后开启

def read_physics_gim_files():
	"""读取配置文件中的gim文件, 只读取名字, 路径过滤掉"""
	try:
		with open('need_small_physics.csv', 'r') as f:
			lines = f.readlines()
			for line in lines:
				# 去掉末尾的回车和
				result = line[:-1].split('\\')
				gim_name = result[-1].split('.')[0]
				physics_gim_files.add(gim_name)
	except Exception as e:
		print e
		print 'read need_small_physics.csv file wrong'
		os.system('pause')


def parse_and_write_scn(scn_name):
	flag = False
	print 'start load file'
	doc = xml.dom.minidom.parse(scn_name)
	print 'success load file'
	models_node = doc.getElementsByTagName('model')
	print 'start parse file'
	for node in models_node:
		name = node.getAttribute('Name')
		gim_name = '_'.join(name.split('_')[:-1])
		print gim_name
		if gim_name in physics_gim_files:
			print gim_name, 'start turn on physics'
			flag = True
			node.setAttribute('Flag', physics_data['Flag'])
			node.setAttribute('ModelFlag', physics_data['ModelFlag'])
			print gim_name, 'success turn on physics'
	print 'success parse file'
	if not flag:
		return
	print 'start write back to file'
	with open(scn_name, 'w') as f:
		doc.writexml(f, addindent='', encoding='utf-8')
	delete_pre_str(scn_name)
	print 'success write back to file'


def delete_pre_str(scn_name):
	with open(scn_name, 'r') as f:
		all_lines = f.readlines()
	with open(scn_name, 'w') as f:
		all_lines[0] = all_lines[0][-7:]
		f.writelines(all_lines)


if __name__ == '__main__':
	print 'start'
	print 'please input the full scn file path'
	path_name = raw_input()
	read_physics_gim_files()
	for scn_file in os.listdir(path_name):
		if scn_file.endswith('.scn'):
			parse_and_write_scn(path_name + '/' + scn_file)
	print 'success !'
	os.system('pause')
