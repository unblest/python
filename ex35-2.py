# a little 'what happens if' scenario
# basically, what happens if I have an 'if' function with an elif, but no else and something happens not covered by the 'if' function?
# turns out that nothing at all happens
# like actually nothing, so if you're expecting the if to return something (value, variable, function kick-off, list or whatever), thou art fucked without an else

response = raw_input("Choose 1 or 2: ")

if response == "1":
    print "You selected 1! Good job!"
elif response == "2":
    print "You selected 2! Good job!"
