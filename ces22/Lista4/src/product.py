from abc import abstractmethod, ABC
from src.taxCalculator import BookTaxCalculator


class Product(ABC):
    '''
    Abstract class for products
    '''

    def __init__(self):
        pass

    @abstractmethod
    def modify(self):
        pass

    @abstractmethod
    def get_taxes(self):
        pass


class Book(Product):
    '''
    Book product class
    '''

    def __init__(self, title, author, genre, edition, publisher, sell_price, buy_price):
        super().__init__()
        self.title = title
        self.author = author
        self.genre = genre
        self.edition = edition
        self.publisher = publisher
        self.sell_price = sell_price
        self.buy_price = buy_price
        self.taxCalculator = BookTaxCalculator()

    def get_taxes(self):
        return self.taxCalculator.get_tax(self.genre, self.sell_price, self.buy_price)

    def get_title(self):
        return self.title

    def modify(self, attr, value):
        if attr == 'title':
            self.title = value
        elif attr == 'buy price':
            self.buy_price = value
        elif attr == 'sell price':
            self.sell_price = value
        elif attr == 'genre':
            self.genre = value
        elif attr == 'edition':
            self.edition = value
        elif attr == 'publisher':
            self.publisher = value
        elif attr == 'author':
            self.author = value
        else:
            print('Unrecognized attribute')

    def get_author(self):
        return self.author
