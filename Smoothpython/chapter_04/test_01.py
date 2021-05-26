# -*- coding: utf-8 -*- 
# @Time     : 2020/8/30 19:20 
# @Author   : wangxiaofeng01@corp.netease.com
# @desc:    : 第四章 文本和字节序列开始


x = '你好世界'
# 查看字节数组
print list(x)
# 查看字节数组中的某一位的二进制
# x[0] 就和 list(x)[0]
# 你
print x[:3].decode('utf8')
print ord(x[0]) & 1, ord(x[0]) & 2, ord(x[0]) & 4, ord(x[0]) & 8
print type(x), type(x.decode('utf8'))
# 也就是说 在python2中, str就是字节数组,转化为list打印即可看到,甚至for loop 都可以
# 所以说,str 作为字节数组,怎么能够进行编码呢? 只能够进行解码


# 转化为ascii(十进制)
print ord('a')
# ascii转化为字符
print chr(97)
x = 'abc'
print ord(x[0])
# ord把字符转化为十进制的ASCII, chr把十进制的ASCII转化为
# 根据张力所言 SACII就是键盘上的一些字符集,2个字节,然后转化为十进制
# unicode就是全部的字符集,所有的长度一样,utf8之类的就是在unicode上面再次编码,让常用的更短,不常用的更长也无所谓


"""源码中能不能使用非ASCII码名称"""
# 看地区吧,西班牙人用西班牙语作为变量名也没什么不好,并且python3源码默认utf8

# fp = open('cafe.txt', 'w')
# fp.write('你好世界,这句话是写进去的')
# fp.close()
fp = open('cafe.txt', 'r')
print fp.read()

# 好了,本章讲的内容跟很有用,但是我选择不看

