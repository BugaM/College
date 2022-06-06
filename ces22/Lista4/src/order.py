from abc import abstractmethod, ABC


class Order(ABC):
    '''
    Abstract class for orders
    '''

    def __init__(self):
        pass

    @abstractmethod
    def modify(self):
        pass

    @abstractmethod
    def print_info(self):
        pass


class BookOrder(Order):
    '''
    Class for book orders
    '''

    def __init__(self, client_name, qtd, price):
        self.client_name = client_name
        self.quantity = qtd
        self.price = price

    def get_cl_name(self):
        return self.client_name

    def print_info(self):
        print('Client name: ' + self.client_name)
        print('Quatity: ' + self.quantity)
        print('Price: ' + self.price)

    def modify(self, attr, value):
        if attr == 'client name':
            self.client_name = value
        elif attr == 'quantity':
            self.quantity = value
        elif attr == 'price':
            self.price = value
        else:
            print('Unrecognized attribute')
