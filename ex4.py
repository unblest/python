# variable test file
# defines number of cars
cars = 100
# defines available space in a car
space_in_a_car = 4.0
# defines number of drivers
drivers = 30
# defines number of passengers
passengers = 90
# defines cars_not_driven as the number of cars minus the number of drivers lets see what happens if we scoot past this thingy
cars_not_driven = cars - drivers
# defines cars_driven as equal to the number of drivers
cars_driven = drivers
# defines the carpool_capacity as number of cars_driven multiplied by the space_in_a_car
carpool_capacity = cars_driven * space_in_a_car
# defines the average_passengers_per_car as equal to the number of passengers divided by the number of cars driven
average_passengers_per_car = passengers / cars_driven


print "There are", cars, "cars avaialble."
print "There are only", drivers, "drivers avaialble."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
print "Hey %s there." % "you"
