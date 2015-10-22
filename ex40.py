# exercise 40: modules, classes and objects

# define the lass 'Song'
class Song(object):
    """Class to define a song's lyrics and then print out the lyrics a line at a time"""
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print line

happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])

bulls_on_parade = Song(["They rally around tha family",
                        "With pockets full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

wrote_writ = Song(["They're taking pictures of the man from God",
                   "I hope his cassock's clean",
                   "The burden of being our holly fellas",
                   "Your halo'd better gleam, better gleam"])

songWords = "Shore to shore, got some land between \nIsland life is living from a cup of broken queens"

shore_to_shore = Song([songWords])

wrote_writ.sing_me_a_song()

shore_to_shore.sing_me_a_song()
