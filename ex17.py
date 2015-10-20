# exercise 17: more files

# import the argv as normal plus some new weird import for an 'exists' module
from sys import argv
from os.path import exists

script, from_file, to_file = argv

# print that we're copying one file to another
print "Copying from %s to %s" % (from_file, to_file)

# define open and read file variables - see note below
# we could do these two on one line, how?
in_file = open(from_file)
indata = in_file.read()

# print the size of the file we opened
print "The input file is %d bytes long" % len(indata)

# this looks like it uses the new exists module to check if the destination file has been created
print "Does the output file exist? %r" % exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()

# this looks like the actual copying of the file to the destination file
# open the thing in write mode and then write to it
out_file = open(to_file, 'w')
out_file.write(indata)

# print completed message
print "Alright, all done"

# close the files
out_file.close()
in_file.close()
