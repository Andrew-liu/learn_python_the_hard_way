# -*- coding:utf-8 -*-

import sys

a = set('abgaglajg')
print a

for i, v in enumerate(['liubin', 'zhangfa', 'zhaofen']) :
    print i, v

questions = ['name', 'quest', 'favorite color']    
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers) :
    print 'What is your {0}? It is {1}. '.format(q, a)

for i  in reversed(range(1, 10, 2)  )  :
    print i

t = ['liubin', 'zhangxin', 'lisi']    
for i in sorted(t) :
    print i

print 1 < 2 == 2   #True 

#print sys.ps1
#print sys.ps2
print dir(sys)

s = 'Hello World'
print str(s)
print repr(s)

for x in range(1, 11) :
    print x, x*x, x*x*x
