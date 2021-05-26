# -*- coding: utf-8 -*- 
# @Time     : 2021/3/19 9:52 
# @Author   : wangxiaofeng01@corp.netease.com
# @desc:    : this is for auto turn on physics in .scn file

import os
import re

scn_path = r'E:\YoungCampusSimulator\client\res\scene\map\mojin_dashijie\mojin_dashijie_content'

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


def process():
	for root, _dirs, files in os.walk(scn_path):
		for _file in files:
			if not _file.endswith('.scn'):
				continue
			file_path = os.path.join(root, _file)
			with open(file_path, 'r') as f:
				content = f.read()
			models = re.findall(r'<model\n.*?</model>', content, re.DOTALL)
			changed = False
			for model in models:
				name_line = re.findall(r'\tName ?= ?".*?"', model)
				if len(name_line) != 1:
					continue

				# 已经开了物理, 但是并没有把寻路关了
				already_turn_on = re.findall(r'\tModelFlag ?= ?"8"', model)
				if len(already_turn_on) >= 1:
					continue
				name_line = name_line[0]
				name = name_line[name_line.find('"')+1: name_line.rfind('"')]
				name = name[:name.rfind('_')]
				if name not in physics_gim_files:
					continue
				if name == 'd_jiaoshi_zhuozi':
					pass
				flag = re.findall(r'\tFlag ?= ?.*?\n', model, re.DOTALL)
				assert len(flag) == 1
				flag = flag[0]
				new_model = model.replace(flag, '\tFlag="4106"\n\t\t\t\t\tModelFlag="8"\n')

				content = content.replace(model, new_model)
				changed = True
			if changed:
				with open(file_path, 'w') as f:
					f.write(content)



if __name__ == '__main__':
	print 'start'
	print 'please input the full scn file path'
	read_physics_gim_files()
	process()
	print 'success !'
