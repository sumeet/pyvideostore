class Movie(object):

    def __init__(self, title):
        self.title = title


class NewReleaseMovie(Movie):

    def calculate_cost(self, days_rented):
        return days_rented * 3

    def calculate_points(self, days_rented):
        return 2 if days_rented > 1 else 1


class ChildrensMovie(Movie):

    def calculate_cost(self, days_rented):
        return (days_rented - 2) * 1.5 if (days_rented) > 3 else 1.5

    def calculate_points(self, days_rented):
        return 1


class RegularMovie(Movie):

    def calculate_cost(self, days_rented):
        if days_rented > 2:
            return 2 + (days_rented - 2) * 1.5
        else:
            return 2

    def calculate_points(self, days_rented):
        return 1
