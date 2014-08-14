# -*- coding:utf-8 -*-

the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'penies', 2, 'dimes', 3, 'quarters']

#注意最后的冒号!!!
for number in the_count :
    print "This is count %d" % number

for fruit in fruits :
    print "A fruit of type : %s " % fruit

for i in change :
    print "I got %r" % i

#empty list
elements = []    

#range()函数会产生小于6的整数 ,可以理解为左开右闭
for i in range(0, 6) :
    print "Adding %d to the list." % i
#append is a function that lists understand
    elements.append(i)

for i in elements :
    print "Element was : %d" % i
