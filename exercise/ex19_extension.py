# -*- coding:utf-8 -*-

def Myfunction(via_one, via_two) :
    print "My First argument is %r" % via_one
    print "My Second argument is %r" % via_two
    print "Thanks you"

Myfunction("hello", "world")
Myfunction(1, 2)
Myfunction(1.3, 2.4)
Myfunction(1 + 6, 2 + 7)
via_one = 100
via_two = 200
Myfunction(via_one, via_two)
Myfunction(via_one + 100, via_two + 200)
Myfunction(via_one + via_two, via_two)
Myfunction('a', 'b')
first = True
second = False
Myfunction(first, second)
Myfunction(3 > 5, 6 > 7)

