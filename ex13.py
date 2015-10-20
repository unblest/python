# exercise 13: parameters, unpacking, variables

# import adds features from python's feature set to your script
#   "features" = modules (and sometimes libraries)
# requesting them keeps programs small and acts as documentation
# argv is "argument variable"
# argv holds the arguments you pass to your script when you run it - i have no idea what that means
from sys import argv

# this "unpacks" the agrv
# it says take whatever is in argv and assign it to the variables on the left in order
script, uno, dos, tres, quatro = argv

quatro = raw_input("Fourth variable: ")

print "The script is called:", script
print "Your first variable is:", uno
print "Your second variable is:", dos
print "Your third variable is:", tres
print "The fourth is:", quatro
