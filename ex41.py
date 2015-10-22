# exercise 41: learning to speak object oriented

# class
    # Tell Python to make a new type of thing
# object
    # two meanings: the most basic type of thing, and any instance of something
    # the archetype/template for a set of data that you pass, or the specific instance of that archetype/template of data
    # archetype would be like order has projectID, items, product total, shipping and tax
    # specific instance would be like order 123456 has projectID 987654, skus 123 and xyz, product total $100, shipping $10, tax $2
# instance
    # what you get when you tell python to create a class
    # basically the second example from above
    # it's the x = class()
# def
    # How you define a function inside a class
# self
    # inside the function in a class, self is a variable for the instance/object being accessed
    # basically, this is how you tell the functions inside of a class how to handle the eventual instances that you create
# inheritance
    # the concept that one class can inherit traits from another class, much like you and your parents
    # I like the example of is-a below better to expalin inheritance
    # a salmon class inherits some of the attributes or charictaristics of a fish class
# composition
    # the concept that a class can be composed of other classes as parts, much like how a car has wheels
    # the metaphor here isn't really the best, but I sort of get it
    # each wheel is a class that defines functions about having breaks and tires made of rubber etc
    # and the car is made of that class and some others about the shape and makeup of the body, and one for the engine and one for the seats inside, etc.
# attribute
    # a property classes have that are from composition and are usually variables
    # things like orderID, amount, ship to address, or whatever
# is-a
    # a phrase to say that something inherits from another, as in 'salmon' is-a 'fish'
# has-a
    # a phrase to say that something is composed of other things or has a trait, as in 'a salmon has-a mouth'
    # at first I thought that this was just for attributes like the salmon/mouth example above
    # but I think this can also be for classes and functions, really anything you can 'compose' a class of
    # so you could probably also say something like salmon has-a function called swim or something like that


# class x(y)
    # make a class named x that is-a y
    # so here y would be the parent class I guess?
    # no idea how that works properly, but it looks essentially like you pass the parent class as a parameter to the child class when you define it
    # as opposed to just leaving it with the standard (object) parameter that seems to be the default
# class x(object):
    # def __init__(self,j)
        # class x has-a __init__ that takes self and j parameters
        # so the __init__ is part of the 'has-a' thingy
# class x(object):
    # def m(self, j)
        # class x has-a function named m that takes self and j as parameters
# foo = x()
    # Set foo to an instance of class x
# foo.m(j)
    # from foo, get the 'm' function and call it with parameters self, j
    # notice that self isn't explicity called out as a parameter of 'm'
    # looks like it's assumed since you're calling the specific instance of x called 'foo'
# foo.k = q
    # from foo, get the k attribute and set it to q
    # this one looks cool, and wasn't fully called out/done in the example
    # the example, doesn't actually call out an attribute/variable k in the class x
    # but assume that you did, youc an redifine the attribute for that instance of that class outside of the class
    # so I imagine you could do something like:
    # orderID123456.margin = orderID123456.prodRev - orderID123456.prodCostActual
