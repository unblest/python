# exercise 35: branches and functions

# import the 'exit' feature from the sys
from sys import exit

# define function 'gold_room' with two if statements
def gold_room():
    print "This room is full of gold. How much do you take?"

    # define variable for user response and logic for if statements
    # if there is a '0' or a '1' in the response, then...
    choice = raw_input("> ")
    if "0" in choice or "1" in choice:
        # how_much variable defined as integer version of user response
        how_much = int(choice)
        # else part declares what happens if user response isn't a number
    else:
        # interesting that this function hasn't been defined yet
        # i suppose that makes sense, since we'll go through, define them all up top, and the script will have the definition by the time the function is actually run
        dead("Man, learn to type a number.")

    if how_much < 50:
        print "Nice, you're not greedy. You win!"
        # here's the mysterious 'exit' feature we improted from sys
        exit(0)
    else:
        dead("You greedy bastard!")

# define new function
def bear_room():
    print "There is a bear here."
    print "The bear has a bunch of honey."
    print "The fat bear is in front of another door"
    print "How are you going to move the bear?"
    # assign starting value for 'bear_moved' variable for next 'while' loop
    bear_moved = False

    # create a while loop
    # i don't fully understand the condition on this one since I don't know what is supposed to be true
    # turns out this makes it an infinite loop (which it needs for the taunt bear and i don't know options)
    # the function ends though with any of the two 'correct' responses
    while True:
        choice = raw_input("> ")

        # some if statements to govern what happens with different responses
        if choice == "take honey":
            dead("The bear looks at you then slaps your face off.")
        # i don't fully understant how the logic is working here
        # i think that it is assuming the value of 'bear_moved' is False
        # so then the choice would be true (true and not (false)) so then, if it's true, print the thing and change the value
        # but if that's the case, then if the value of bear_moved is true already, this won't fire, and instead, it will fire the next section where you die
        # maybe the assumption is that it will never be true to start (which I think is correct since it's defined at the beginning of the function)
        # but maybe not since this is a 'while' loop and could run again after changing the variable value?
        # speaking of, why the fuck is this a while loop?
        elif choice == "taunt bear" and not bear_moved:
            print "The bear has moved from the door. You can go through it now."
            bear_moved = True
        elif choice == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print "I got no idea what that means."


# define a new function for cthulhu_room
def cthulhu_room():
    print "Here you see the great evil Cthulhu."
    print "He, it, whatever stares at you and you go insane."
    print "Do you flee for your life or eat your head?"

    choice = raw_input("> ")

    # interesting way to grab different variations of a user input here
    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("Well that was tasty!")
    else:
        cthulhu_room()

# define a new function for when the users chooses poorly and dies
# the argument 'why' is always the string passed when executing the function in the other functions
def dead(why):
    print why, "Good job!"
    exit(0)

# define a new function for the start of the story
def start():
    print "You are in a dark room."
    print "There is a door to your right and left."
    print "Which one do you take?"

    choice = raw_input("> ")

    # if you choose the left door, run the bear_room function
    if choice == "left":
        bear_room()
    # if you choose the right door, run the cthulhu_room function
    elif choice == "right":
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve")

# now we just need to run the start function to kick everything off
start()
