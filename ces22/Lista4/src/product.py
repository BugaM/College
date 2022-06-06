from abc import abstractmethod, ABC

class Product(ABC):
      def __init__(self):
            pass
      
      @abstractmethod
      def modify(self):
            pass

      @abstractmethod
      def get_taxes(self):
            pass

class Book(Product):
      def __init__(self, title, author, genre, edition, publisher, sell_price, buy_price):
          super().__init__()
          self.title = title
          self.author = author
          self.genre = genre
          self.edition = edition
          self.publisher = publisher
          self.sell_price = sell_price
          self.buy_price = buy_price
          
      def get_taxes(self):
            pass

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
          
      


