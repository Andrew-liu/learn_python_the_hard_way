# -- coding : utf-8 --

#print function will change line, the '\n' too ,
#so it will change the line for twice
print "how old are you?\n",
age = raw_input()

# , was use to forbid changing line
print "how tall are you?",
height = raw_input()


#to use input sth
print "how much do you weight ?\n",
weight = raw_input() 

name = raw_input("name : ")
print name

newname = input("newname : ")
print newname

print "so, you're %r old, %r tall and %r heavy ." % (age, height, weight)
