import unittest

from customer import Customer
from movie import Movie
from rental import Rental


class VideoStoreTest(unittest.TestCase):

    def setUp(self):
        self.customer = Customer('Fred')

    def test_single_new_release_statement(self):
        self.customer.add_rental(Rental(Movie('The Cell', Movie.NEW_RELEASE), 3))
        self.assertEquals('Rental Record for Fred\n\tThe Cell\t9\nYou owed 9\nYou earned 2 frequent renter points\n', self.customer.statement())

    def test_dual_new_release_statement(self):
        self.customer.add_rental(Rental(Movie('The Cell', Movie.NEW_RELEASE), 3))
        self.customer.add_rental(Rental(Movie('The Tigger Movie', Movie.NEW_RELEASE), 3))
        self.assertEquals('Rental Record for Fred\n\tThe Cell\t9\n\tThe Tigger Movie\t9\nYou owed 18\nYou earned 4 frequent renter points\n', self.customer.statement())

    def test_single_childrens_statement(self):
        self.customer.add_rental(Rental(Movie('The Tigger Movie', Movie.CHILDRENS), 3))
        self.assertEquals('Rental Record for Fred\n\tThe Tigger Movie\t1.5\nYou owed 1.5\nYou earned 1 frequent renter points\n', self.customer.statement())

    def test_multiple_regular_statement(self):
        self.customer.add_rental(Rental(Movie('Plan 9 from Outer Space', Movie.REGULAR), 1))
        self.customer.add_rental(Rental(Movie('8 1/2', Movie.REGULAR), 2))
        self.customer.add_rental(Rental(Movie('Eraserhead', Movie.REGULAR), 3))

        self.assertEquals('Rental Record for Fred\n\tPlan 9 from Outer Space\t2\n\t8 1/2\t2\n\tEraserhead\t3.5\nYou owed 7.5\nYou earned 3 frequent renter points\n', self.customer.statement())


if __name__ == '__main__':
    unittest.main()
