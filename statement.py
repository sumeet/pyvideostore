class Statement(object):

    def __init__(self, name):
        self.name = name
        self._rentals = []

    def add_rental(self, rental):
        self._rentals.append(rental)

    def generate(self):
        self._clear_totals()
        return (self._make_header() + self._make_rental_lines() +
                self._make_footer())

    def _clear_totals(self):
        self.total_amount = 0
        self.frequent_renter_points = 0

    def _make_header(self):
        return 'Rental Record for %s\n' % self.name

    def _make_rental_lines(self):
        statement_text = ""
        for rental in self._rentals:
            statement_text += self._make_rental_line(rental)
        return statement_text

    def _make_rental_line(self, rental):
        self.frequent_renter_points += rental.rental_points
        self.total_amount += rental.amount
        return '\t%s\t%s\n' % (rental.title, rental.amount)

    def _make_footer(self):
        return ('You owed %.1f\n'
                'You earned %d frequent renter points\n' %
                    (self.total_amount, self.frequent_renter_points))
