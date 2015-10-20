# exercise 29: what if
# intro to the 'if' statement! Woot!

# define some variables
people = 40
cats = 30
dogs = 15

# let the 'if' statements begin and conditionaly print stuff based on variable values
if people < cats:
    print "Too many cats! The world is doomed!"

if people > cats:
    print "Not many cats! The world is saved!"

if people < dogs:
    print "The world is drooled on!"

if people > dogs:
    print "The world is dry!"

if dogs != cats:
    print "Cats and dogs out of balance. World is doomed."

# adjust the value of the 'dogs' variable
dogs += 5

if people >= dogs:
    print "People are greater than or equal to dogs."

if people <= dogs:
    print "People are less than or equal to dogs"


if people == dogs:
    print "People are dogs."
