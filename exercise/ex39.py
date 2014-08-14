# -*- coding:utf-8 -*-

ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "Wait there's not 10 things in that list, let's fix that."

stuff = ten_things.split(' ') #分解成了list
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10 :
    next_one = more_stuff.pop() #末尾出栈
    print "Adding:", next_one
    stuff.append(next_one) #末尾添加
    print "There's %d items now ." % len(stuff)

print "There we go :", stuff #输出整个list

print stuff[1]#输出第二个元素
print stuff[-1]#倒数第一个元素
print stuff.pop()#最后一个出栈
print ' '.join(stuff)#' '.join(things) 其实是join(' ', things),用' ' 连接整个list 
 
print '#'.join(stuff[3 : 5])


