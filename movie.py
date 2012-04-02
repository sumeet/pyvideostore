class Movie(object):

    REGULAR = 0
    NEW_RELEASE = 1
    CHILDRENS = 2

    def __init__(self, title, price_code):
        self.title = title
        self.price_code = price_code

    def rental_points(self, days_rented):
        if (self.price_code == Movie.NEW_RELEASE and days_rented > 1):
            return 2
        else:
            return 1

    def amount(self, days_rented):
        if self.price_code == Movie.REGULAR:
            rental_amount = 2
            if days_rented > 2:
                rental_amount += (days_rented - 2) * 1.5
        elif self.price_code == Movie.NEW_RELEASE:
            rental_amount = days_rented * 3
        elif self.price_code == Movie.CHILDRENS:
            rental_amount = 1.5
            if days_rented > 3:
                rental_amount += (days_rented - 3) * 1.5
        return rental_amount
