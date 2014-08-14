# -*- coding:utf-8 -*-

from sys import argv

# 使用argv命令行传参
script, filename = argv

#打开文件,获取的文件标示符赋给txt 'file'类型
txt = open(filename)

print type(txt)

#读取文件内容输出
print "type the filename again :%s"  % filename
print txt.read()

#再次输入文件名,
print "type thre filename again: "
file_again = raw_input("> ")

#打开文件
txt_again = open(file_again)

#读取文件
print txt_again.read()

#关闭文件
txt.close()
txt_again.close()

