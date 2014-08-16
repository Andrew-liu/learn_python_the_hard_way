# -*- coding:utf-8 -*-

a = 0
b = 1
print a
while b < 1000:
    print b,  #逗号截止可以禁止输入换行
    a, b = b , a + b


def fib(n) : 
    a = 0
    b = 1
    t = a
    lis = []
    print 'new'
    while b < n :
        lis.append(b)
        t = a
        a = b
        b = t + a
    return lis    

i = 256 * 256
print '\nthe value  i is', i


x = 0
for x in range(1, 20, 2) :
    print x 

print range(1, 30, 3)    

while x < 100: 
    x += 1
    pass


fib(100)

print '\n'
def change(a):
    a = 10
nfoo = 2
change(nfoo)
print nfoo

print fib(100)

def f(a, L = None) :
    if L is None :
        L = []
    L.append(a)
    return L

print f(1)
print f(2)
print f(3)
