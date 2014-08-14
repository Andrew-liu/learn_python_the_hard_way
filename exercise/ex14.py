# -*- coding:utf-8 -*-

from sys import argv

script, user_name = argv
prompt = '谭二蛋> '

print "hi, %s, I'm the %s script." % (user_name, script)
print "I'd like to ask question"
print "Do you like me %s ?" % user_name
likes = raw_input(prompt)

print "live where %s ?" %user_name
lives = raw_input(prompt)

print "What kind computer like?"
computer = raw_input(prompt)

print """
so you said %r about liking me.
your live in %r, not sure where that is.
and you have a %r compuer. nice
""" % (likes, lives, computer)


