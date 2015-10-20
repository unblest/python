# exercise 36: designing and debugging
# goal is to create my own version of the choose your own adventure app from the last exercise

# import the argv to have the user provide the monster pack they want to use
from sys import argv
script, monster_file = argv

# open file variable
open_monster = open(monster_file)

# need to add the contents of the file to the monster_list now
# start with assigning the contents of the file as a string to a variable
monster_file_contents = open_monster.read()

# split out the file contents into a list
monsters_split = monster_file_contents.split('\n')

# assign monster variables using list variable
roomLeftMonster = monsters_split.pop(0)
roomMiddleMonster = monsters_split.pop(0)
roomRightMonster = monsters_split.pop(0)


def dead(howIDie):
    print howIDie
    exit()


# define treasure room function
# four options and a death
# else of typing mush
def treasure():
    print """
    You have reached the treasure room
    You may now choose your prize
    Select from the following:
    1.  A literal boat load of cash
    2.  Tyrant for eternity
    3.  World peace
    4.  One novelty beer koozie
    """

    # don't actually need the while loop - you can just run the function again (but it prints out the thing above too)
    # while loop to prompt again until valid selection made
    while True:

        # define input variable
        # need the variable here to prompt again when the loop runs back
        prize = raw_input("Choose now, and choose wisely...")

        # if statement for all of the possible responses
        if prize in ("1", "cash"):
            print """
            Here is a toy boat stuffed with cash. Hope you like Zimbabwean dollars.
            Watch out for that exchange rate!
            print "Now get out of here you greedy bastard!
            """
            exit()
        elif prize in ("2", "tyrant"):
            print "Who's more tyranical than a meter maid? You shall henceforth wander parking meters and ticket people who are just late for work for eternity."
            print "Off you go you petty tyrant you!"
            exit ()
        elif prize in ("3", "peace"):
            print "Well aren't you just a bleeding hearted saint. Fine. Peace it is. Schmuck."
            print "Go and enjoy your utopia. Schmuck"
            exit ()
        elif prize in ("4", "beer"):
            print "Seriously? Seriously? You. Have. Chosen. Poorly."
            dead("You will now drown in warm beer for eternity for requesting a beer koozie over world peace. Fucking beer koozie.")
            exit()
        else:
            print "Pick one of the options listed. Don't just make shit up!!! I'm not a fucking genie!"


# define function for middle room to select responses based on monster pack
# run appropriate function for the monster pack selected
def middleDoor():
    if monster_file == "normal_pack.txt":
        middleMonsterNormal()
    elif monster_file == "monty_python_pack.txt":
        middleMonsterMonty()
    else:
        print "Honestly, I don't know how the script could run and get this far"


# define the middleMonsterNormal function for all of the responses for the middle room with the normal_pack of monsters selected
def middleMonsterNormal():
    print """
    Passing through the middle door you see a dark and smoky room.
    You can't be sure, but you feel a presence.
    You're being watched.
    Suddenly, out of the shadows leaps a %s, all in black.
    You can barely make him out, but the gleam of the katana
    Seems to give away the Ninja's intentions.
    This indominable assassin now stands between you and the door to your freedom.
    """ % roomMiddleMonster

    print """
    How will you face this deadly foe?
    1.    Challenge the Ninja to a battle of wits to the death!
    2.    HADOUKEN!!!
    3.    Take off my pants to distract the %s and gain the advantage!
    """ % roomMiddleMonster

    # define ninja response variable
    ninjaFight = raw_input("Choose now, and choose wisely...")

    # if statements for all of the different responses
    if ninjaFight in ("1", "wits"):
        print "The %s isn't Golem from LOTR! While you're thinking of your first riddle, he just slices your face right off." % roomMiddleMonster
        dead("""
        As your face slowly slides off your head,
        the *ching* of the katana still ringing in what's left of your ears,
        you suddenly realize your error before falling down dead
        """)
    elif ninjaFight in ("2", "HADOUKEN!!!"):
        print "You reach back and launch your HADOUKEN!!! blast at the %s disintigrating him instantly!" % roomMiddleMonster
        print "The Ninja is dead. You may now pass into the treasure room."
        treasure()
    elif ninjaFight in ("3", "pants"):
        print """
        So horrified by your grotesque figure, even in the dark room,
        the Ninja turns the blade on himself and falls to the ground dead.
        You awkwardly and ashamedly pull up your pants and walk into the treasure room
        """
        treasure()
    else:
        print """
        The ninja is unphased by... whatever it was that you just typed.
        A quick flash of the blade is the last thing you see before you die.
        """
        dead("""
        \"Damn it!!! I should have just picked one of the predetermined responses!\"
        is all you can think as you float up to heaven,
        or maybe the other thing you naughty person
        """)

# define the function for middleMonsterMonty monster pack responses
def middleMonsterMonty():
    print """
    Passing through the middle door, you walk into a misty forest from another time
    Up ahead, you see a small bridge over a tiny creek
    Standing in resolute silence in front of the bridge is a towering knight in menacing black armor.
    As you approach he bellows out \"None shall pass!\"
    It is clear that to continue in your quest for the grail, you must face this %s
    """ % roomMiddleMonster

    print """
    How will you defeat the mighty %s?
    1.    Hurl insults at the knight!
    2.    Use the Holy Hand Grenade of Antioch
    3.    Callously dismember the knight limb by limb
    """ % roomMiddleMonster

    # define the black knight response variable
    blackKnightFight = raw_input("Choose now, and choose wisely...")

    # if statements for all of the different responses
    if blackKnightFight in ("1", "insults"):
        print "The knight shouts back \"I asked for an arguement, not these insults!\""
        dead("The knight charges at you with his mighty broadsword and chops your head off.")
    elif blackKnightFight in ("2", "Holy Hand Grenade of Antioch"):
        print """
        After consulting the instructions, you pull the pin and begin to count before throwing the grenade.
        \"One. Two. Five!\"
        """
        dead("Having skipped over the number 'three' the grenade explodes in your hand, killing you and Patsy instantly")
    elif blackKnightFight in ("3", "dismember"):
        print """
        Every time the brave sir knight charges out you, you hack off a limb
        leaving just a torso hurling insults as you walk through the forest to the treasure room.
        """
        treasure()
    else:
        print """
        The black knight is unphased by... whatever it was that you just typed.
        He charges you with his mighty broadsword and lops off your head.
        """
        dead("""
        \"Damn it!!! I should have just picked one of the predetermined responses!\"
        is all you can think as you float up to heaven,
        or maybe the other thing you naughty person
        """)


# define function for left room to select responses based on monster pack
# run appropriate function for the monster pack selected
def leftDoor():
    if monster_file == "normal_pack.txt":
        leftMonsterNormal()
    elif monster_file == "monty_python_pack.txt":
        leftMonsterMonty()
    else:
        print "Honestly, I don't know how the script could run and get this far"

# define function and responses for left room if normal_pack is selected
def leftMonsterNormal():
    print """
    You only get the left door about half open before hearing a terifying roar.
    Pausing, you peer through the door and see a huge %s.
    I can really only describe it as seething with anger and hunger.
    """ % roomLeftMonster

    print """
    How would you like to handle the large, striped and very irritated feline in front of you?
    1.    Let me just toss it this steak I had in my back pocket and sneak by.
    2.    I'm pretty sure I can take a tiger! Hand to hand combat bitch!
    3.    You know, I bet one of these other doors doesn't have a %s behind it. Let me try one of those.
    """ % roomLeftMonster

    # define tigerFight user response variable
    tigerFight = raw_input("Choose now, and choose wisely...")

    if tigerFight in ("1", "steak"):
        print """
        You have a steak in your back pocket?
        What are you a butcher?
        Fine, you toss in the steak and the tiger begins snacking on it.
        """
        dead("""
        Unfortunately, as you start sneaking by, the tiger spots you and simply sees you as a bigger steak.
        You are devoured.
        Thanks for playing!
        """)
    elif tigerFight in ("2", "combat"):
        print """
        You've decided to fight a tiger with your bear hands.
        This isn't going to go well for you my friend.
        """
        dead("""
        Unsurprisingly, the tiger parries your karate chop by driving his huge, sharp teeth into your neck.
        You're now just another meal for a tiger inexplicably being kept in this room
        just to murder anyone foolish enough to enter it.
        """)
    elif tigerFight in ("3", "flee"):
        print """
        Deciding to flee does sound like a good idea.
        Honestly, how are you going to beat a tiger?
        """
        mainRoom()
    else:
        print """
        The tiger is unphased by... whatever it was that you just wrote.
        He simply leaps on you and begins devouring you alive.
        """
        dead("""
        \"Damn it!!! I should have just picked one of the predetermined responses!\"
        is all you can think as you float up to heaven,
        or maybe the other thing you naughty person
        """)

# define function and responses for left room if monty_python_pack is selected
def leftMonsterMonty():
    print """
    You open the door and see a white, fuzzy bunny rabbit in the room.
    Strangely, it seems to be surrounded by bones, but it's soooo fuzzy!
    """

    print """
    How would you like to proceed?
    1.    It's so cute! I bet it's a good luck charm to get to the treasure.
          I'll go pick it up and take it with me!
    2.    I've seen this movie sir, and you're not fooling me!
          Brother Maynard! Bring up the Holy Hand Grenade of Antioch!
    3.    I don't trust these bones...
          Back away slowly and try one of the other doors
    """

    # define bunnyFight user response variable
    bunnyFight = raw_input("Choose now, and choose wisely...")

    if bunnyFight in ("1", "cute"):
        print """
        Looks can be deceiving!
        That's no ordinary, harmless bunny rabbit! It's a %s
        """ % roomLeftMonster
        dead("""
        As you approach the rabbit, it suddenly leaps up and chews your head off.
        You're now just another skeleton in the rabbit's horrible lair
        """)
    elif bunnyFight in ("2", "Holy Hand Grenade of Antioch"):
        print """
        After consulting the instructions, you pull the pin and begin to count before throwing the grenade.
        \"One. Two. Five!\"
        """
        dead("Having skipped over the number 'three' the grenade explodes in your hand, killing you and Patsy instantly")
    elif bunnyFight in ("3", "flee"):
        print """
        You wisely ascertain that not all is right with this bunny situation.
        Surely one of the other doors has better options behind it.
        """
        mainRoom()
    else:
        print """
        The %s is unphased by... whatever it was that you just wrote.
        He simply leaps on you and begins devouring you alive.
        """ % roomLeftMonster
        dead("""
        \"Damn it!!! I should have just picked one of the predetermined responses!\"
        is all you can think as you float up to heaven,
        or maybe the other thing you naughty person
        """)


# define function for right room to select responses based on monster pack
# run appropriate function for the monster pack selected
def rightDoor():
    if monster_file == "normal_pack.txt":
        rightMonsterNormal()
    elif monster_file == "monty_python_pack.txt":
        rightMonsterMonty()
    else:
        print "Honestly, I don't know how the script could run and get this far"

# define function and responses for right room if normal_pack is selected
def rightMonsterNormal():
    print """
    Opening the door on the right, you find yourself confronted by a hungry %s
    \"Brrrrrrraaaaaaaaaaaiiiiiiinnnnnnnnnnnsssssssss\" it growls as it turns and begins to lumber towards you
    Suddenly, you lock eyes with the zombie and you feel a strange power corrupting you.
    It dawns on you that this is no ordinary zombie.
    """ % roomRightMonster

    print """
    How will you deal with the risen dead and it's strange, entrancing power?
    1.    It's just one zombie and I've seen Day of the Dead like 47 times! Here comes an axe to the face!
    2.    ...wha? I... the zombie is... calling to me. I... I want to hug it...
    3.    What wizardry is this?!?!? Must... Resist... Zombie... Magic!!! Must... Run... Away!!!
    """

    # define zombieFight user response variable
    zombieFight = raw_input("Choose now, and choose wisely...")

    # if statements for all of the different responses
    if zombieFight in ("1", "axe"):
        print """
        As you raise the axe you inexplicably found above your head,
        You suddenly lock eyes with the zombie again.
        Staring into the black, dead eyes, your arms go heavy and you become transfixed
        It all makes sense now. The world is a lie.
        The only truth is the nihilist hedonism of the zombie.
        """
        dead("Brrrrrrraaaaaaaaaaaiiiiiiinnnnnnnnnnnsssssssss!!!")
    elif zombieFight in ("2", "hug"):
        print """
        Unable to break away from the zombie's compelling gaze, you become transfixed
        It all makes sense now. The world is a lie.
        The only truth is the nihilist hedonism of the zombie.
        """
        dead("You and the zombie hug it out and venture out in search of tasty, tasty brains.")
    elif zombieFight in ("3", "run away"):
        print """
        Realizing the hypnotizing effect of the souless, zombie eyes staring back at you,
        You tear your gaze away and run back the way you came in abject terror.
        Close call my friend. Now see what horrors await behind the other doors!
        """
        mainRoom()
    else:
        print """
        Despite... whatever it was you just typed, you can't seem to avert your gaze.
        The black, souless eyes of the zombie call to you in ways that seem to shatter reality itself.
        You're transfixed.
        It all makes sense now. The world is a lie.
        The only truth is the nihilist hedonism of the zombie.
        """
        dead("""
        Not that your brain is capable of rational thought any longer, but if it were,
        You would be cursing yourself for not simply having selected one of the predetermined responses.
        """)

# define the function for the right to run the monty_python_pack responses
def rightMonsterMonty():
    print """
    Walking through the door on the right, you see before you
    a giant chasm with a rickety rope and plank bridge spanning it.
    *it looks a bit like a bridge of death*
    As you apprach the bridge, you see that the old man from scene 24 stands at the foot of the bridge
    Before venturing across, you must answer his questions three
    Ere the other side you see!
    """
    questionOne = raw_input("WHAT is you name? ")
    questionTwo = raw_input("WHAT is your quest? ")
    questionThree = raw_input("WHAT airspeed of an unladen swallow? ")

    if questionThree == "What do you mean, an African or European swallow?":
        print """
        The old man from scene 24 looks puzzled and spurts out:
        \"Huh? What? I... I don't know that...\"
        and he is suddenly flung into the air and is cast down into the Gorge of Eternal Peril.
        However, on the way down, the rush of air from his falling body collapse the bridge.
        There is now no way across the Gorge of Eternil Peril.
        You must go back and find another way.
        """
        mainRoom()
    else:
        print "WRONG!!!"
        dead("You are suddenly grabbed by a magical force, hoisted into the air and flung into the Gorge of Eternal Peril!")


# define the mainRoom function
def mainRoom():
    print """
    Welcome, welcome weary traveller!
    As you can see, there are three doors before you.
    Behind each door lies... who knows what?
    But, should you keep your wits about you, I promise you a treasure at the end.

    Which door will you choose?
    1.    The door on the left
    2.    The door in the middle
    3.    The door on the right
    """
    firstDoor = raw_input("So choose now, and choose wisely...")

    # if statements to select which function to run
    if firstDoor in ("1", "left"):
        leftDoor()
    elif firstDoor in ("2", "middle"):
        middleDoor()
    elif firstDoor in ("3", "right"):
        rightDoor()
    else:
        print "Please just type 1, 2 or 3 to select your door."
        mainRoom()

mainRoom()
