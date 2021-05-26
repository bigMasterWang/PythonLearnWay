# -*- coding: utf-8 -*- 
# @Time     : 2021/5/25 20:13 
# @Author   : wangxiaofeng01@corp.netease.com
# @desc:    :

# 导入时, 运行时
"""
导入时会"运行全部顶层代码", 但是顶层代码会经过一些加工(例如运行时的语句, 连接数据库等)
import语句可以触发任何运行时的行为

"""
# 去看 evaltiem.py