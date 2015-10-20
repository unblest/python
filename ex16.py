# exercise 16: reading and writing files

# define the argv per usual
from sys import argv

script, filename = argv

# print some prompts for a raw_input to follow
print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

# raw_input for the response
# CTRL-C must like close the script I guess?
# RETURN just allows the script to progress and delete the file
raw_input("?")

# print some stuff and open the file to do stuff
# don't know what the 'w' is for in the open function
print "Opening the file..."
target = open(filename, 'w')

# print some stuff and truncate/delete the target variable (file)
print "Truncating the file. Goodbye!"
target.truncate()

# ask for three lines with raw_input
print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")
cheatsy = "%s \n %s \n %s \n" % (line1, line2, line3)

# now we write the lines to the file we just truncated
# study exercise to condence the number of write lines to one
print "I'm going to write these to the file."

target.write(cheatsy)

# and now we close the file to save the changes
print "And finally, we close it."
target.close()
