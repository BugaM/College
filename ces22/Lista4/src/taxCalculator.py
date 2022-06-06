from abc import ABC, abstractmethod


class TaxCalculator(ABC):
    '''
    Abstract class to calculate taxes
    '''

    def __init__(self):
        pass

    @abstractmethod
    def get_tax(self):
        pass


class BookTaxCalculator(TaxCalculator):
    '''
    Class that calculates book related taxes
    '''

    def __init__(self):
        super().__init__()

    def get_tax(self, genre, sell_price, buy_price):
        if genre == 'education':
            return 0
        return (sell_price - buy_price)*0.3
