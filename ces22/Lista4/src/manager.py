from abc import ABC, abstractmethod
from person import Client

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
      pass

class OrderManager(Manager):
      pass
