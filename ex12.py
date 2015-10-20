# exercise 12: prompting people

# rewrite the last exercise to use just prompts rather than strings followed by inputs
# define variables with prompts
age = raw_input("How old are you? ")
height = raw_input("How tall are you? ")
weight = raw_input("How much do you weight? ")

print "So, you're %r old, %r tall and %r heavy." % (age, height, weight)
