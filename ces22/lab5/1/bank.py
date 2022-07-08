from abc import abstractmethod, ABC

from tkinter import *
from tkinter import ttk

from datetime import datetime


class Command(ABC):
      """
      Abstract class for command design pattern
      """
      def __init__(self, gui, account):
          self.gui = gui
          self.account = account
      
      @abstractmethod
      def execute(self):
            """
            Executes button
            """
            pass

class Account:
      """
      Bank account
      """
      def __init__(self, money, credit):
            self.money = money
            self.credit = credit
      
      def withdraw(self, qt):
            if float(qt) <= self.money:
                  self.money -= float(qt)
            
      
      def receive_transfer(self, qt):
            self.money += qt
      
class WithdrawComman(Command):

      def __init__(self, gui, account):
          super().__init__(gui, account)

      def execute(self):
          value = self.gui.withdraw_entry.get()
          if float(value) > 0:
            self.account.withdraw(value)
            self.gui.data['text'] = 'Saque realizado no valor de {}'.format(value)
            self.gui.operation_history += 'Saque realizado no valor de {}: {}\n'.format(value, self.gui.get_current_datetime())

class CreditCommand(Command):
      def __init__(self, gui, account):
          super().__init__(gui, account)

      def execute(self):
          self.gui.current_op['text'] = 'Crédito:'
          value = self.account.credit
          self.gui.operation_history += 'Crédito checado - total {} : {}\n'.format(value, self.gui.get_current_datetime())
          self.gui.data['text'] = str(self.account.credit)

class BalanceCommand(Command):
      def __init__(self, gui, account):
          super().__init__(gui, account)

      def execute(self):
          self.gui.current_op['text'] = 'Saldo:'
          value = self.account.money
          self.gui.operation_history += 'Saldo checado - total {} : {}\n'.format(value, self.gui.get_current_datetime())
          self.gui.data['text'] = self.account.money

class OperationsHistoryCommand(Command):
      def __init__(self, gui, account):
          super().__init__(gui, account)

      def execute(self):
          self.gui.current_op['text'] = 'Operações realizadas:'
          self.gui.data['text'] = self.gui.operation_history


class Invoker:
      '''
      Invoker for commands
      '''

      def __init__(self, gui, account):
            self.gui = gui
            self.account = account

            self.withdraw_command = WithdrawComman(gui, self.account)
            self.credit_command = CreditCommand(gui, self.account)
            self.balance_command = BalanceCommand(gui, self.account)
            self.op_history_command = OperationsHistoryCommand(gui, self.account)
            
      def withdraw(self):
            self.withdraw_command.execute()
      
      def show_credit(self):
            self.credit_command.execute()
      
      def show_balance(self):
            self.balance_command.execute()
      
      def show_operation_history(self):
            self.op_history_command.execute()


class GUI:
      """
      Tkinter GUI
      """
      def __init__(self, root, account):
            invoker = Invoker(self, account)
            self.operation_history = ''

            root.title("Banco ITA")

            frm = ttk.Frame(root)
            frm.grid(column=4, row=4)

            self.withdraw_label = ttk.Label(frm, text="Valor a sacar:")
            self.withdraw_label.grid(column=1, row=1, sticky=W)

            self.withdraw_entry = ttk.Entry(frm)
            self.withdraw_entry.insert(0,"0")

            self.withdraw_entry.grid(column=1, row = 2, sticky=W)

            withdraw_button = ttk.Button(frm, text='Sacar', command=invoker.withdraw)
            withdraw_button.grid(column=1,row=3, sticky=W)

            balance_button = ttk.Button(frm, text='Saldo', command=invoker.show_balance)
            balance_button.grid(column=1, row = 4, sticky=W)

            credit_button = ttk.Button(frm, text='Crédito', command=invoker.show_credit)
            credit_button.grid(column=1, row = 5, sticky=W)

            operation_history_button = ttk.Button(frm, text="Histórico de operações", command=invoker.show_operation_history)
            operation_history_button.grid(column=1, row=6, sticky=W)

            # Column 2
            self.current_op = ttk.Label(frm, text= "Selecione sua operação")
            self.current_op.grid(column=2, row= 1, sticky=W)

            self.data = ttk.Label(frm, text='')
            self.data.grid(column=2, row=2, sticky=E)



      def get_current_datetime(self):

            return datetime.now().strftime("%d/%m/%Y - %H:%M:%S")

if __name__ == "__main__":
    root = Tk()
    account = Account(2000,1000)
    GUI(root, account)

    root.mainloop()

    