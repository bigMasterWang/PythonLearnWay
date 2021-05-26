# -*- coding: utf-8 -*- 
# @Time     : 2021/5/17 20:07 
# @Author   : wangxiaofeng01@corp.netease.com
# @desc:    :
# 显示下载进度并处理错误


# from tqdm import tqdm
# import time
# for i in tqdm(range(1000)):
# 	time.sleep(.01)

# 现在由threading模块, 更加高级,
# 进程futures.ProcessPoolExecutor, 但是现在也有更加高级的用法 multiprocessing
# 一个i/o密集型, 一个cpu密集型