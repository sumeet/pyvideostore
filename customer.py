from movie import Movie


class Statement(object):

    def __init__(self, customer_name):
        self.customer_name = customer_name
        self._rentals = []

    def add_rental(self, rental):
        self._rentals.append(rental)

    def generate(self):
        return self._header() + self._rental_lines() + self._footer()

    @property
    def amount_owed(self):
        return sum(rental.cost for rental in self._rentals)

    @property
    def frequent_renter_points(self):
        return sum(rental.points for rental in self._rentals)

    def _header(self):
        return 'Rental Record for %s\n' % self.customer_name

    def _rental_lines(self):
        return ''.join(self._rental_line(rental) for rental in self._rentals)

    def _rental_line(self, rental):
        return '\t%s\t%s\n' % (rental.title, rental.cost)

    def _footer(self):
        return ('You owed %s\n'
                'You earned %d frequent renter points\n' % (
                    self.amount_owed, self.frequent_renter_points))
