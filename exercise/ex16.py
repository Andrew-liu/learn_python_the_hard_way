# -*- coding:utf-8 -*-

from sys import argv

script, filename = argv

print "we are going erase %r ." % filename
print "if you don't want that hit c+c"
print "if you want to that hit return "

raw_input("?")

#以写的形式打开文件
print "opening the file ..."
target = open(filename, 'w')

#删除文件中所有内容
print "truncating the file. good bye"
target.truncate()

line1 = raw_input("line1 :")
line2 = raw_input("line2 :")
line3 = raw_input("line3 :")

print "i'm going to write these to the file ."

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

target.write("%s,%s,%s" % (line1, line2, line3))

print "and finally . we close it"
target.close()


