# exercise 39: dictionaries, oh lovely dictionaries

# create a mapping of state to abbreviation
# curly brackets denotes defining a dictionary
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

# create a basic set of states and some cities in them
cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

# add some more cities
# looks like to add an element to the dictionary, you square bracket the key on the left and assign it to equal whatever is on the right of the =
cities['NY'] = 'New York City'
cities['OR'] = 'Portland'

# print out some cities
# I'm guessing this prints 10 dashes?
print '-' * 10
# I think this is saying print the assigned element in the cities list at 'position' 'NY' using the square brackets
print "NY state has: ", cities['NY']
print "OR state has: ", cities['OR']

# print some states
print '-' * 10
print "Michigan's abbreviation is: ", states['Michigan']
print "Florida's abbreviation is: ", states['Florida']

# do it by using the state and then cities dict
print '-' * 10
print "Michigan has: ", cities[states['Michigan']]
print "Florida has: ", cities[states['Florida']]

# print every state abbreviation
# using a for loop to do this
# interesting that it uses the 'abbrev' variable/thingy which doesn't seem to have been defined
# also uses the 'items' modifier which I don't fully understand
print '-' * 10
for state, abbrev in states.items():
    print "%s is abbreviated %s" % (state, abbrev)

# print every city in state
print '-' * 10
for abbrev, city in cities.items():
    print "%s has the city %s" % (abbrev, city)

# now do both at the same time
print '-' * 10
for state, abbrev in states.items():
    print "%s state is abbreviated %s and has city %s" % (state, abbrev, cities[abbrev])

print '-' * 10
# safely get an abbreviation by state that might not be there
state = states.get('Texas')

if not state:
    print "Sorry, no Texas."

cities['TX'] = 'Dallas'    

# get a city with a default value
# I don't fully understand what's going on here
# looks like we're doing the safe check to see if there is a city/state for Texas
# but I don't get why we're sort of passing the extra argument of 'Does Not Exist'
# maybe I can go back and add a city for TX and see if is going to do a return one or the other type of thing
# or if it will reassign 'Does Not Exist' as the name of the city stored in the dictionary
# I don't think it will reassign since that would be something like cities['TX'] = 'Dallas'
city = cities.get('TX', 'Does Not Exist')
print "The city for the state 'TX' is: %s" % city
