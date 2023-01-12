from project.movie_specification.movie import Movie


class Thriller(Movie):
    _age_restriction = 16

    def __init__(self, title, year, owner, age_restriction=16):
        super().__init__(title, year, owner, age_restriction)

