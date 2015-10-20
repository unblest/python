# exercise 25: even more practice

# function to break words using new 'split' modifier
# interesting use of triple quotes for the string in the function
def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words

# function to sort words using new 'sorted' command
def sort_words(words):
    """Sorts the words."""
    return sorted(words)

# function to print the first word using 'pop' modifier
def print_first_word(words):
    """Prints the first word after popping it off."""
    word = words.pop(0)
    print word

# function to print the last word
# looks like it works the same as the function above, but just uses a different 'pop' value
def print_last_word(words):
    """Prints the last word after popping it off"""
    word = words.pop(-1)
    print word

# function to take a full sentence and return the sorted words
# passing the arugment 'sentence' between functions in this function
# this function also runs two of the above functions
#   the first to break the sentence given, and the second to sort the result of the broken words
def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

# function to print the first and last words of a sentence
# this function uses three of the above functions
def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

# finally a function to do all of the basic functions above at once
# break the sentence, sort the words, and return the first and last words
def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
