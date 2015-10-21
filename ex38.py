# exercise 38: doing things to lists

# define global variable 'ten_things'
ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "Wait, there are not 10 things in that list. Let's fix that."

# split the variable into individual words and assign them to a list variable 'stuff'
stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

# while loop to append stuff up to 10 things from what I can tell
# while loop is true as long as the length of the list 'stuff' doesn't equal 10
# probably should have made this less than to prevent any possible situation of
# getting the list length to 11 and then running the loop for infinity
while len(stuff) != 10:
    # pops off the next word on the list more_stuff
    next_one = more_stuff.pop()
    print "Adding: ", next_one
    # running the append 'function' that we haven't defined at all which doesn't make sense to me
    stuff.append(next_one)
    print "There are %d items now." % len(stuff)

print "There we go: ", stuff

print "Let's do some things with stuff"

# not a clue what this will do
# first one here prints the element of the list at cardinal position 1 (2nd position)
print stuff[1]
# second one here looks like it prints the element at the end of the list (if cardinal 0 is first, then -1 would be last I suppose)
print stuff[-1] # whoa! fancy he says
# third one pops off corn and prints it
print stuff.pop()
# fourth one joins all of the elements of the list together and separates them with a space ' '
print ' '.join(stuff) # what? cool! he says
# last one looks like it joins the elements at cardinal position 3 and 4 (ranges, like 3:5 in this case, ignore the last number in the range)
print '#'.join(stuff[3:5]) # super stellar! he says
