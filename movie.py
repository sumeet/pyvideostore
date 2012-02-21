class Movie(object):

    CHILDRENS = 2
    REGULAR = 0
    NEW_RELEASE = 1

    def __init__(self, title, price_code):
        self._title = title
        self._price_code = price_code

    @property
    def price_code(self):
        return self._price_code

    @price_code.setter
    def price_code(self, code):
        self._price_code = code

    @property
    def title(self):
        return self._title
