# study exercise for exercise 15: reading files

from sys import argv

script, filename = argv

txt = open(filename)

print "Here's your file %r:" % filename
print txt.read()

txt.close()
