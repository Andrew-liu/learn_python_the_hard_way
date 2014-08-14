# -*- coding:utf-8 -*-

#函数定义
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket.\n"

#通过两个常量调用函数
print "We can just give the function numbers directly :"    
cheese_and_crackers(20, 30)

#通过两个变量调用函数
print "OR, we can use variables from out script :"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

#通过常量数学计算传参调用函数
print "We can even do math inside too :"
cheese_and_crackers(10 + 20, 5 + 6)

#通过变量+常量传参
print "And we can combine the two, variables and math :"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

