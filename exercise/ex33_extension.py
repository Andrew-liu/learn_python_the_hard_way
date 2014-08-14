# -*- coding:utf-8 -*-

def while_loop(num, index = 1) :
    i = 0
    numbers = []
    while i < num :
        numbers.append(i)
        print "Numbers is :", numbers
        i += index
    for x in numbers :
        print "Number in numbers is %d" % x

def for_loop(num) :
    for x in range(0, num) :
        numbers = []
        numbers.append(x)
        print "Numbers : ", numbers


while_loop(10, 2)       
for_loop(10)
