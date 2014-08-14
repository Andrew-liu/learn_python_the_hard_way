# -- coding : utf-8 --

tabby_cat = "\tI'm tabbed in ."
persion_cat  = "I'm split\non a line ."
backslash_cat = "I'm \\ a \\ cat ."

# string block
fat_cat = """
I'll do a list :
\t* cat fodd
\t* fishies
\t* catnip\n\t* grass
"""

#similar with upper
fat_c = '''
hello\twordl
l\n
love\n
you
'''

fat_ex = " %r, %r, %r, %r" % ("st\"ring\'", 1, 2, 'hell')


print tabby_cat
print persion_cat
print backslash_cat
print fat_cat
print fat_c
print fat_ex
