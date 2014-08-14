# -*- coding:utf-8 -*-

from sys import argv

script, filename = argv

print "I will open the filename %s" % filename
txt = open(filename)

print "I will read it"
print txt.read()

print "I will close it"
txt.close()
