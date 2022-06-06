from abc import ABC, abstractmethod

class Person(ABC):
      def __init__(self, cpf, name, email) -> None:
          self.cpf = cpf
          self.name = name
          self.email = email

      @abstractmethod
      def modify(self, attr, value):
            pass

class Client():
      def __init__(self, cpf, name, email) -> None:
          self.cpf = cpf
          self.name = name
          self.email = email

      def modify(self, attr, value):
            if attr == 'name':
                  self.name = value
            elif attr == 'email':
                  self.email = value
            else:
                  print('Unrecognized attribute')
      
      def get_cpf(self):
            return self.cpf
      
      def print_info(self):
            print('Name: ' + self.name)
            print('Email: ' + self.email)