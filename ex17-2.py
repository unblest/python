# see how short I can make exercise 17 script to copy files
# goal is one line
# minus the notes of course

from sys import argv

script, from_file, to_file = argv

in_file = open(from_file).read()

out_file = open(to_file, 'w').write(in_file)
