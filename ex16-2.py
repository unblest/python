# write a script to read the file I created in exercise 16 using read and argv

# import the argv feature
from sys import argv

# define argv with a variable
script, filename = argv

# define variable to open file
txt = open(filename)

# print the contents of the file
print txt.read()

# close the fucker
txt.close()
