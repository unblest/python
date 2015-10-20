# exercise 30: else and if

# define some variables
people = 30
cars = 30
trucks = 30


# let the 'if' and 'elif' (else-if) and 'else' statements begin
if cars > people:
    print "We should take the cars."
elif cars < people:
    print "We should not take the cars."
else:
    print "We can't decide"

if trucks > cars:
    print "That's too many trucks."
elif trucks < cars:
    print "Maybe we could take the trucks."
else:
    print "We still can't decide"

if people > trucks:
    print "Alright, let's just take the trucks."
else:
    print "Fine, let's stay home then."

# redefine the variables
people += 10
cars -= 5
trucks -=20

# new, complex boolean in the 'if'
if people > (cars + trucks) and cars != trucks:
    print "We have more people than vehicles. We'll need to carpool."
elif people == (cars + trucks):
    print "We have just enough vehicles for each person."
else:
    print "EVERYONE PANIC!!! Too many vehicles!"

# let's try to make this a function to easily run with with changing variable values
def if_cars(people, cars, trucks):
    if people > (cars + trucks) and cars != trucks:
        print "We have more people than vehicles. We'll need to carpool."
    elif people == (cars + trucks):
        print "We have just enough vehicles for each person."
    else:
        print "EVERYONE PANIC!!! Too many vehicles!"

if_cars(people, cars, trucks)

# redefine the variables
people += 10
cars += 5
trucks += 5

if_cars(people, cars, trucks)

# redefine the variables to make cars and trucks equal
people = 20
cars = 10
trucks = 10

if_cars(people, cars, trucks)
