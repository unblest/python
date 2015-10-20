# strings and text exercise

# defining of the variables
x = "there are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

# print the variable strings
print x
print y

# print strings with the variables
print "I said: %r" % x
print "I also said: '%s'." % y

# more variables
hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

# print the new variables with the goofy, undefined %r
print joke_evaluation % hilarious

# left anf right vairable definition
w = "this is the left side of..."
e = "a string with a right side."

print w + e
