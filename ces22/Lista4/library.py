from manager import ClientManager, BookManager

class Library:
      def __init__(self):
           self.clientManager = ClientManager()
           self.bookManager = BookManager()
      
      # Client methods
      def add_client(self, cpf, name, email):
            self.clientManager.add(cpf, name, email)           
      def check_client(self, cpf):
            self.clientManager.get_info(cpf)
      def modify_client(self, cpf, attr, value):
            self.clientManager.modify(cpf, attr, value)
      def remove_client(self, cpf):
            self.clientManager.remove(cpf)
      