# variable strings exercise
# define the variables
name = "Brian Loughry"
age = 35 # not a lie
height_inches = 74.0 # inches
weight_pounds = 180.0 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

# convert to metric
weight_kg = weight_pounds / 2.2
height_cm = height_inches * 2.54

# print the things using variable strings
print "Let's talk about %s." % name
print "He's %d inches tall." % height_inches
print "He's %d pounds heavy." % weight_pounds
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair" % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# print the metrics
print "He's %d centimeters tall" % height_cm
print "He's %d kilograms heavy" % weight_kg

# the trixy line with the uber complicated variable string
# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % ( age, height_inches, weight_pounds, age + height_inches + weight_pounds)
