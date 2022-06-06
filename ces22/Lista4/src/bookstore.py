from src.manager import ClientManager, BookManager, AuthorManager, BookOrderManager


class Bookstore:
    '''
    Bookstore class 
    '''

    def __init__(self):
        self.client_manager = ClientManager()
        self.book_manager = BookManager()
        self.author_manager = AuthorManager()
        self.book_order_manager = BookOrderManager()

    # Client methods
    def add_client(self, cpf, name, email):
        self.client_manager.add(cpf, name, email)

    def check_client(self, cpf):
        self.client_manager.get_info(cpf)

    def modify_client(self, cpf, attr, value):
        self.client_manager.modify(cpf, attr, value)

    def remove_client(self, cpf):
        self.client_manager.remove(cpf)

    # Author methods

    def add_author(self, name, email):
        self.author_manager.add(name, email)

    def add_book_to_author(self, book):
        self.author_manager.add_book(book)

    def check_author_books(self, author_name):
        self.author_manager.get_author_books(author_name)

    def modify_author(self, name, attr, value):
        self.author_manager.modify(self, name, attr, value)

    def remove_author(self, name):
        self.author_manager.remove(name)

    def remove_book_from_author(self, author_name, title):
        self.author_manager.remove_book_from_author(author_name, title)

    # Book methods

    def add_book(self, title, author, genre, edition, publisher, sell_price, buy_price):
        book = self.book_manager.add(
            title, author, genre, edition, publisher, sell_price, buy_price)
        try:
            self.author_manager.add_book(author, book)
        except:
            self.author_manager.add(author, None)
            self.author_manager.add_book(author, book)

    def modify_book(self, book_title, attr, value):
        self.book_manager.modify(book_title, attr, value)

    def remove_book(self, book_title):
        book = self.book_manager.remove(book_title)
        self.remove_book_from_author(book.get_author(), book_title)

    # Order methods

    def add_order(self, client_name, qtd, price):
        self.book_order_manager.add(client_name, qtd, price)

    def check_order(self, client_name):
        self.book_order_manager.get_info(client_name)

    def modify_order(self, client_name, attr, value):
        self.book_order_manager.modify(client_name, attr, value)

    def remove_order(self, client_name):
        self.book_order_manager.remove(client_name)
