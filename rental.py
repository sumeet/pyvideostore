from movie import Movie


class Rental(object):

    def __init__(self, movie, days_rented):
        self.movie = movie
        self.days_rented = days_rented

    @property
    def rental_points(self):
        if (self.movie.price_code == Movie.NEW_RELEASE and
            self.days_rented > 1):
            return 2
        else:
            return 1

    @property
    def amount(self):
        if self.movie.price_code == Movie.REGULAR:
            rental_amount = 2
            if self.days_rented > 2:
                rental_amount += (self.days_rented - 2) * 1.5
        elif self.movie.price_code == Movie.NEW_RELEASE:
            rental_amount = self.days_rented * 3
        elif self.movie.price_code == Movie.CHILDRENS:
            rental_amount = 1.5
            if self.days_rented > 3:
                rental_amount += (self.days_rented - 3) * 1.5
        return rental_amount

    @property
    def title(self):
        return self.movie.title
