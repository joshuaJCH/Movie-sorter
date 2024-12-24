class Database:
    def get_movies(self):
        movies = []
        with open('Media to consume.txt', 'r') as file:
            lines = file.readlines()
            for line in lines:
                movies.append

class Movie:
    def __init__(self, watched, title, length, genre, synopsis):
        self.watched = watched
        self.title = title
        self.length = length
        self.genre = genre
        self.synopsis = synopsis
