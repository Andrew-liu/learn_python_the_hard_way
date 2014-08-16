# -*- coding:utf-8 -*-

def cheeseshop(kind,  *arguments, **keywords) :
    print "--Do you have any ", kind, "?"
    print "--I'm sorry, we're all out of", kind
    for arg in arguments :
        print arg
    print "-" * 40
    keys = sorted(keywords.keys())
    for kw in keys :
        print kw, ":", keywords[kw]


cheeseshop("Limburger", 
           "It's very runny, sir.",
           "It's really very, Very runny.",
           shopkeeper = "Michael Palin",
           client = "John Cleese",
           sketch = "Cheese Shop Sketch")       

a = ['liubin', 'suqing', 'tanjunxin', 'lule', 'nanshen']
del a[0]
print a
del a[2 : 4]
print a
del a[ : ]
print a

t = 123, 456, 789
print t

# t[0] = 124   tuple是不可以修改的

x, y, z = t
print x, y, z
name = set(a)
print name
