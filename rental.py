from movie import Movie


class Rental(object):

    def __init__(self, movie, days_rented):
        self.movie = movie
        self.days_rented = days_rented

    @property
    def rental_points(self):
        return self.movie.rental_points(self.days_rented)

    @property
    def amount(self):
        return self.movie.amount(self.days_rented)

    @property
    def title(self):
        return self.movie.title
