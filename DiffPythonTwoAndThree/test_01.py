# 这个__dict__在python2中有很多公用的属性，而在python3中就变成了只有自己本身的属性
import sys
class A:
	pass
a = A()
a.flush = sys.stdout.flush
old_print, sys.stdout = sys.stdout, a
def new_print(*args, **kwargs):
	if '\n' in args:
		return
	old_print.write('print process\n')
	old_print.write(*args, **kwargs)
a.write = new_print
print('你好世界')

