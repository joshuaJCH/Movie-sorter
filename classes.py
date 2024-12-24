class Database

class Movie:
    def __init__(self, watched, title, length, genre, synopsis):
        self.watched = watched
        self.title = title
        self.length = length
        self.genre = genre
        self.synopsis = synopsis

    def get_movies(self):
        with open('Media to consume.txt')