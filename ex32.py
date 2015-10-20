# exercise 32: loops and lists
# loops are things that repeat a thing (action, command, function or whatever) a bunch of times
# lists store a list of value someplace (can assign them to variables for example)
# i think i actually misunderstood this a bit
# the reason these two are bundled together is that most of the time, you're going to want a loop action on a bunch of items in a list
# this is essentially like saying, for all costs on brand x, update price to be cost + 10 or something

# assign some lists to some variables
# note the mix of integers and strings in the third variable
the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# first 'for-loop'
# looks like you assign a new variable for each value in the list and run the loop
# this first kind of for-loop goes through a list
for number in the_count:
    print "This is count %d" % number

# same as above for 'fruits'/strings
for fruit in fruits:
    print "A fruit type of %s" % fruit

# also we can go through mixed lists too
# notice we have to use %r since we don't know what's in it
for i in change:
    print "I got %r" % i

# we can also build lists, first start with an empty one
elements = []

# then use the range function to do 0 to 5 counts
for i in range(0, 6):
    print "adding %d to the list." % i
    # append is a function that lists understand
    # this is the command that actually builds the list
    # so the for loop runs through the given range and then prints the thing and then adds it to the list stored on the 'elements' variable
    elements.append(i)

# now we can print them out too
for i in elements:
    print "Element was: %d" % i
