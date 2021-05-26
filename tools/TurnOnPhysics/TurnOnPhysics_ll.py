# -*- coding: utf-8 -*- 
# @Time     : 2021/3/19 9:52 
# @Author   : wangxiaofeng01@corp.netease.com
# @desc:    : this is for auto turn on physics in .scn file

import xml.dom.minidom
import os
import re

scn_path = r'E:\YoungCampusSimulator\client\res\scene\map\mojin_dashijie\mojin_dashijie_content'

physics_gim_files = set()

physics_data = {
	'Flag': '4106',
	'ModelFlag': '8'
}

model_number = 0

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


def process():
	global model_number
	for root, _dirs, files in os.walk(scn_path):
		for _file in files:
			if not _file.endswith('.scn'):
				continue
			file_path = os.path.join(root, _file)
			with open(file_path, 'r') as f:
				content = f.read()
			models = re.findall(r'<model\n.*?</model>', content, re.DOTALL)
			for model in models:
				name_line = re.findall(r'\tName = ".*?"', model)
				assert len(name_line) == 1
				name_line = name_line[0]
				name = name_line[name_line.find('"')+1: name_line.rfind('"')]
				name = name[:name.rfind('_')]
				if name not in physics_gim_files:
					continue
				flag = re.findall(r'\tFlag =.*?\n', model, re.DOTALL)
				assert len(flag) == 1
				flag = flag[0]
				new_model = model.replace(flag, '\tFlag = "4106"\n\t\t\t\t\tModelFlag = "8"\n')
				content = content.replace(model, new_model)
				model_number += 1
			with open(file_path, 'w') as f:
				f.write(content)



if __name__ == '__main__':
	print 'start'
	print 'please input the full scn file path'
	# path_name = raw_input()
	read_physics_gim_files()
	# for scn_file in os.listdir(path_name):
	# 	if scn_file.endswith('.scn'):
	# 		parse_and_write_scn(path_name + '/' + scn_file)
	process()
	print 'success !'
	# os.system('pause')
	print 'model_number: {}'.format(model_number)
