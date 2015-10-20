# exercise 14: prompting and passing

# the import modules thing that I don't fully understand
from sys import argv

# defining argv - this time with a prompt!
script, user_name, department = argv
prompt = 'Put your answer here mutha fucka! '

# print some stuff and define variable with raw_input at the end
print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

# new argument and print
print "Why on earth do you work in the %s department?" % department
reasons = raw_input(prompt)

# uses argv inputted user name and asks where user lives
print "Where do you live %s?" % user_name
lives = raw_input(prompt)

# same as above minus user_name variable string
print "What kind of computer do you have?"
computer = raw_input(prompt)

# prints results with inputted variables
print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" % (likes, lives, computer)
