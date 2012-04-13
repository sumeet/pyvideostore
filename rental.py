from movie import Movie


class Rental(object):

    def __init__(self, movie, days_rented):
        self.movie = movie
        self.days_rented = days_rented

    @property
    def title(self):
        return self.movie.title

    @property
    def points(self):
        return self.movie.calculate_points(self.days_rented)

    @property
    def cost(self):
        return self.movie.calculate_cost(self.days_rented)
