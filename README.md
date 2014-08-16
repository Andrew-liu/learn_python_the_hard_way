#Python 语法总结


---


#1. 基础语法总结
> #主要用与单行注释 """三双引号用于块注释

> 数组计算主要接触到 + - * / 以及符合运算 += -= *= /=

> Python是一种动态语言, 不需要刻意声明变量的类型, 系统会识别出来, 具体实现有待考证, 'print type(变量名)'刻意获取变量的类型

> 字符串可用单引号和双引号引起, 自己推荐使用双引号, 与字符相区分

> Python中打印目前主要接触的函数为print ,后面可以跟各种类型的变量,非常方便

> 需要注意格式化输出, 类似与C语言中的占位符, %s %d %r %d %f ,主要格式为 
    print "%r, %d, %s" % (via1, via2, via3) //多个变量用逗号分开

Waring : 注意区分 %s, %r

###1.1.0 转义字符
>  print "You \'d need to know \'bout escapes with \\ t    hat do \n newline and \t tabs"

当在字符串中想要打印"时, 可以在"加\


##1.1. unpack和import 命令行处理

> 与系统的IO输入输出交互, 主要使用了这个函数raw_input() , '括号中可以输入提示用语'

> import的使用,现在感觉类似于C/C++中的include
> 使用准则为范例
    from sys import argv //类似C中main函数的参数
    script, first = argv //可以直接在运行脚本的时候动态确定变量的内容


##1.2. 文件基本操作

> 读取文件使用函数fd = open(filename) 函数返回一个file类型的变量,类似与linux下的文件描述符和标准C的FILE *

- fd.read() '读取文件'
- fd.seek(offset) '文件读取指针的时候的偏移'
- fd.close() '打开文件最后一定要记得关闭'
- otherwise, open(filename, 'w') '以读的方式打开'
- fd.truncate(size)  '无参的时候擦出文件所有数据,带size的时候我理解为文件指针偏移后删除'

---

#2. 函数语法

> def functionname(via, via ...) :  '不要忘记冒号'
'定义第二行一定要使用tab缩进'

> 函数可以有返回值, 最后使用return返回,无需像C/C++一样设置返回值类型

`**可以一次返回多个返回值**`

##2.1. 常用函数

range(), 填写需要的数字范围,是一个左闭右开的空间
example : range(0, 6)产生0 -5 六个数字

---

#3. Python基础逻辑

对与if语句:会通过缩进来判断执行的语句,如果不缩进会报错'IndentationError : expected an indented block'
> 行尾的冒号的作用是告诉 Python 接下来你要创建一个新的代码区段。
> 如果你的某一行是以 : (冒号, colon)结尾,那就意味着接下来的内容是一个新的代码片段,新的代码片段是需要被缩进的。

>  and or not 与或非三大逻辑,并可以放在一起使用

##3.1.1. 判断

```python
if condition :
    exe
elif condition :
    exe
else :
    exe //程序框架
```

##3.1.2 循环
> 两大循环 while_loop for_loop

```python

for x in range(0,num): //直接满足条件才结束
    exe

while i < 6:  //while表达式为False停止,
    exe
```
**主要函数: range()**
**打印函数: print()**

---

#4. Data structure

##4.1 list

    list_.append(sth) //在list_添加内容
    list_.count() //计算大小
    ten_things.split(' ') //此函数会将整句字符串的话转化为list

```python

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


```


##4.2. dictionary(dicts, dict)

1. 类似于C++中的map用法
2. dict本身是无序的,要求key唯一,key可以是个函数
3. 通过del dictionary['city']
4. print stuff.items() 生成list[(key, value)]

```

es = {'CA' : 'San Francisco', 'MI' : 'Detroit', 'FL' : 'Jacksonville'}

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
#通过key就可以调用函数
    city_found = cities['_find'](cities, state)
    print city_found

```


