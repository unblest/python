# exercise 15: reading files

# import the argument variable per "normal"
from sys import argv

# define the input for the file name we're going to read
script, filename = argv

# define and new variable with the open verb which is new
txt = open(filename)

# print the contents of the file
print "Here's your file %r:" % filename
print txt.read()

# now asks for the file name again and assigns to a new variable
print "Type the file name again:"
file_again = raw_input("> ")

# define another variable to open the filename given
txt_again = open(file_again)

# print the results
print txt_again.read()

txt.close()
txt_again.close()
