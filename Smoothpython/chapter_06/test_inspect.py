# -*- coding: utf-8 -*- 
# @Time     : 2021/1/6 22:07 
# @Author   : wangxiaofeng01@corp.netease.com
# @desc:    :

import inspect
import old_test_01

pomoros = [func_name for func_name, func in inspect.getmembers(old_test_01, inspect.isfunction) if func_name.endswith('Promotion')]
print pomoros