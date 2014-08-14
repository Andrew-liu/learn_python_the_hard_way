# -*- coding:utf-8 -*-
#directory / hash

#list
things = ['a', 'b', 'c', 'd']
print things

things[1] = 'z' #会将原来第二位的元素覆盖
print things[1]


#hash_map
print things

stuff = {'name' : 'Zed', 'age' : '36', 'height' : 6 * 12 + 2}
print stuff['name']

print stuff['age']

print stuff['height']

stuff['city'] = "San Francisco"
print stuff['city']

#添加键值对
stuff[1] = "Wow"
stuff[2] = "Neato"

print stuff[1]
print stuff[2]
print stuff  #输出整个dict

#del删除字典中的键值对
del stuff['city']
del stuff[1]
del stuff[2]

print stuff.items()


