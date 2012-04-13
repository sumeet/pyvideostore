from expecter import expect
import unittest

from customer import Statement
from movie import ChildrensMovie, Movie, NewReleaseMovie, RegularMovie
from rental import Rental


class VideoStoreTest(unittest.TestCase):

    def setUp(self):
        self.statement = Statement('Fred')
        self.new_release_1 = NewReleaseMovie('New Release 1')
        self.new_release_2 = NewReleaseMovie('New Release 2')
        self.childrens = ChildrensMovie('Childrens')
        self.regular_1 = RegularMovie('Plan 9 from Outer Space')
        self.regular_2 = RegularMovie('8 1/2')
        self.regular_3 = RegularMovie('Eraserhead')

    def test_single_new_release_statement(self):
        self.statement.add_rental(Rental(self.new_release_1, 3))
        self.statement.generate()
        expect(self.statement.frequent_renter_points) == 2
        expect(self.statement.amount_owed) == 9

    def test_dual_new_release_statement(self):
        self.statement.add_rental(Rental(self.new_release_1, 3))
        self.statement.add_rental(Rental(self.new_release_2, 3))
        self.statement.generate()
        expect(self.statement.frequent_renter_points) == 4
        expect(self.statement.amount_owed) == 18

    def test_single_childrens_statement(self):
        self.statement.add_rental(Rental(self.childrens, 3))
        self.statement.generate()
        expect(self.statement.frequent_renter_points) == 1
        expect(self.statement.amount_owed) == 1.5

    def test_multiple_regular_statement_totals(self):
        self.statement.add_rental(Rental(self.regular_1, 1))
        self.statement.add_rental(Rental(self.regular_2, 2))
        self.statement.add_rental(Rental(self.regular_3, 3))
        self.statement.generate()
        expect(self.statement.frequent_renter_points) == 3
        expect(self.statement.amount_owed) == 7.5

    def test_multiple_regular_statement_formatting(self):
        self.statement.add_rental(Rental(self.regular_1, 1))
        self.statement.add_rental(Rental(self.regular_2, 2))
        self.statement.add_rental(Rental(self.regular_3, 3))
        self.assertEquals(
            'Rental Record for Fred\n'
            '\tPlan 9 from Outer Space\t2\n'
            '\t8 1/2\t2\n'
            '\tEraserhead\t3.5\n'
            'You owed 7.5\nYou earned 3 frequent renter points\n',
            self.statement.generate())


if __name__ == '__main__':
    unittest.main()
