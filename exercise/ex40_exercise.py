# -*- coding:utf-8 -*-

cities = {'CA' : 'San Francisco', 'MI' : 'Detroit', 'FL' : 'Jacksonville'}

cities['NY'] = 'New York'
cities['OR'] = 'Portland'

def find_city(themap, state) :
    if state in themap :
        return themap[state]
    else :
        return "Not Found"

#将函数放入map 并起名为_find 表示两者有相同意义
cities['_find'] = find_city

while True :
    print "State? (ENTER to quit)",
    state = raw_input("> ")
    if not state : break  #终止循环
    city_found = cities['_find'](cities, state)
    print city_found
