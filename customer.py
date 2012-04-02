from movie import Movie


class Statement(object):

    def __init__(self, name):
        self.name = name
        self._rentals = []

    def add_rental(self, rental):
        self._rentals.append(rental)

    def generate(self):
        self.total_amount = 0
        self.frequent_renter_points = 0
        rentals = self._rentals
        result = 'Rental Record for ' + self.name + '\n'

        for rental in rentals:
            this_amount = 0

            # determines the amount for each line
            if rental.movie.price_code == Movie.REGULAR:
                this_amount += 2
                if rental.days_rented > 2:
                    this_amount += (rental.days_rented - 2) * 1.5
            elif rental.movie.price_code == Movie.NEW_RELEASE:
                this_amount += rental.days_rented * 3
            elif rental.movie.price_code == Movie.CHILDRENS:
                this_amount += 1.5
                if rental.days_rented > 3:
                    this_amount += (rental.days_rented - 3) * 1.5

            self.frequent_renter_points += 1

            if (rental.movie.price_code == Movie.NEW_RELEASE and
                rental.days_rented > 1):
                self.frequent_renter_points += 1

            result += '\t' + rental.movie.title + '\t' + str(this_amount) + '\n'
            self.total_amount += this_amount

        result += 'You owed ' + str(self.total_amount) + '\n'
        result += 'You earned ' + str(self.frequent_renter_points) + ' frequent ' \
                  'renter points\n'

        return result
