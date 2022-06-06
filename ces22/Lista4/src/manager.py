from abc import ABC, abstractmethod
from src.product import Book
from src.person import Author, Client

class Manager(ABC):
      def __init__(self) -> None:
          self.obj = []
      
      @abstractmethod
      def add(self):
            pass

      @abstractmethod
      def modify(self):
            pass

      @abstractmethod
      def remove(self):
            pass

class ClientManager(Manager):
      def __init__(self) -> None:
          super().__init__()

      def add(self, cpf, name, email):
            cl = Client(cpf, name, email)
            self.obj.append(cl)
      
      def get_info(self, cpf):
            for cl in self.obj:
                if cl.get_cpf() == cpf:
                      cl.print_info()
                      return
            print('Client not found')
      
      def modify(self, cpf, attr, value):
            for cl in self.obj:
                if cl.get_cpf() == cpf:
                      cl.modify(attr, value)
                      return
            print('Client not found')
                
      def remove(self, cpf):
            for cl in self.obj:
                if cl.get_cpf() == cpf:
                      self.obj.remove(cl)
                      return
            print('Client not found')


class BookManager(Manager):
      def __init__(self):
          super().__init__()
      
      def add(self, title, author, genre, edition, publisher, sell_price, buy_price):
            book = Book(title, author, genre, edition, publisher, sell_price, buy_price)
            self.obj.append(book)
            return book

      def modify(self, title, attr, value):
            for book in self.obj:
                if book.get_title() == title:
                      book.modify(attr, value)
                      return
            print('Book not found')

      def remove(self, title):
            for book in self.obj:
                if book.get_title() == title:
                      self.obj.remove(book)
                      return
            print('Book not found')

class AuthorManager(Manager):
      def __init__(self):
          super().__init__()
      
      def add(self, name, email):
            author = Author(name,email)
            self.obj.append(author)
      
      def add_book(self, author_name, book):
            for auth in self.obj:
                  if auth.get_name() == author_name:
                        auth.add_book(book)
                        return
            raise Exception('Author not found')
      
      def get_author_books(self, author_name):
            for auth in self.obj:
                  if auth.get_name() == author_name:
                        for book in auth.get_books():
                              print(book.get_title())
                        return
            print('Author not found')
      
      def modify(self, name, attr, value):
            for auth in self.obj:
                if auth.get_name() == name:
                      auth.modify(attr, value)
                      return
            print('Author not found')
      
      def remove(self, name):
            for auth in self.obj:
                if auth.get_name() == name:
                      self.obj.remove(auth)
                      return
            print('Author not found')

class OrderManager(Manager):
      pass
