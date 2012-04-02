class NewReleaseMovie(object):

    def __init__(self, title):
        self.title = title

    def rental_points(self, days_rented):
        return 2 if days_rented > 1 else 1

    def amount(self, days_rented):
        return days_rented * 3


class ChildrensMovie(object):

    def __init__(self, title):
        self.title = title

    def rental_points(self, days_rented):
        return 1

    def amount(self, days_rented):
        rental_amount = 1.5
        if days_rented > 3:
            rental_amount += (days_rented - 3) * 1.5
        return rental_amount


class RegularMovie(object):

    def __init__(self, title):
        self.title = title

    def rental_points(self, days_rented):
        return 1

    def amount(self, days_rented):
        rental_amount = 2
        if days_rented > 2:
            rental_amount += (days_rented - 2) * 1.5
        return rental_amount
