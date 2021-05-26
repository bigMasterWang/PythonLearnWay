# -*- coding: utf-8 -*- 
# @Time     : 2021/5/13 11:34 
# @Author   : wangxiaofeng01@corp.netease.com
# @desc:    : 读取ags中的数据, 作为标准数据, 转化为表格


import xml.dom.minidom
import xlwt

OBJ_ID = '-1'

result = []


# 使用yield, 读一行, 写一行
# 或者使用多线程, 边读边写

def parse_ags():
	doc = xml.dom.minidom.parse('male_student_body.ags')
	transit_info = doc.getElementsByTagName('TransitInfo')[0]
	for transit_node in transit_info.childNodes:
		if transit_node.nodeName == '#text':
			continue
		for anim_name, time in transit_node.attributes.items():
			if anim_name == 'TransitTime':
				continue
			if ',' in time:
				result.append((transit_node.nodeName, anim_name, time.split(',')[1]))
			else:
				result.append((transit_node.nodeName, anim_name, time.split(',')))


def write_excel():
	workbook = xlwt.Workbook(encoding='utf-8')
	worksheet = workbook.add_sheet('anim_graph_transit_data')
	for index in xrange(0, len(result), 1):
		item = result[index]
		# 行index, 列index
		worksheet.write(index + 1, 0, item[0])
		worksheet.write(index + 1, 1, item[1])
		worksheet.write(index + 1, 2, float(item[2]))
	workbook.save('anim_graph_transit_data.xls')


if __name__ == '__main__':
	parse_ags()
	write_excel()
