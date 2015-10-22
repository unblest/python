# exercise 41: OOP reading test

# ok so we're importing modules here
# the first one does something random apparently
# the second one is the url library he mentioned and it's grabing something that probably opens a url in the code
# I'm guessing that's how we open the url with the txt file to assign the WORD_URL variable
import random
from urllib import urlopen
import sys

# so open the text file from the website with the list of words
# then create an empty list for the words to eventually go into (I'm guessing)
WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

# create a dictionary with the phrases set as the key-value pairs/tuples
PHRASES = {
    "class %%%(%%%):":
      "Make a class named %%% that is-a %%%",
    "class %%%(object): \n\tdef __init__(self, ***)" :
      "class %%% has-a __init__ that takes self and *** parameters.",
    "class %%%(object): \n\tdef ***(self, @@@)":
      "class %%% has-a function named *** that takes self and @@@ parameters.",
    "*** = %%%()":
      "Set *** to an instance of class %%%.",
    "***.***(@@@)":
      "From *** get the *** function, and call it with parameters self, @@@.",
    "***.*** - '***'":
      "From *** get the *** atribute and set it to '***'."
}

# do they want to drill phrases first
# an if statement that checks to find the length of the argv inputted by the user
# it also checks to see if the second thing in the argv list equals the string 'english'
# if both are true, it sets the PHRASE_FIRST variable to true
# looks like this checks to see if we want to drill on phrases first
if len(sys.argv) == 2 and sys.argv[1] == "english":
    PHRASE_FIRST = True
else:
    PHRASE_FIRST = False

# load up the words from the website
# does a for loop for each word in the website and reads each line... i guess
# then it appends the list stored in 'WORD' with the stripped word from each line
for word in urlopen(WORD_URL).readlines():
    WORDS.append(word.strip())

def convert(snippet, phrase):
    class_names = [w.capitalize() for w in
                   random.sample(WORDS, snippet.count("%%%"))]
    other_names = random.sample(WORDS, snippet.count("***"))
    results = []
    param_names = []               
