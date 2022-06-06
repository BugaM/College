from src.manager import ClientManager, BookManager, AuthorManager, OrderManager


class Bookstore:
    def __init__(self):
        self.clientManager = ClientManager()
        self.bookManager = BookManager()
        self.authorManager = AuthorManager()
        self.orderManager = OrderManager()

    # Client methods
    def add_client(self, cpf, name, email):
        self.clientManager.add(cpf, name, email)

    def check_client(self, cpf):
        self.clientManager.get_info(cpf)

    def modify_client(self, cpf, attr, value):
        self.clientManager.modify(cpf, attr, value)

    def remove_client(self, cpf):
        self.clientManager.remove(cpf)

    # Author methods

    def add_author(self, name, email):
        self.authorManager.add(name, email)

    def add_book_to_author(self, book):
        self.authorManager.add_book(book)

    def check_author_books(self, author_name):
        self.authorManager.get_author_books(author_name)

    def modify_author(self, name, attr, value):
        self.authorManager.modify(self, name, attr, value)

    def remove_author(self, name):
        self.authorManager.remove(name)

    def remove_book_from_author(self, author_name, title):
        self.authorManager.remove_book_from_author(author_name, title)

    # Book methods

    def add_book(self, title, author, genre, edition, publisher, sell_price, buy_price):
        book = self.bookManager.add(
            title, author, genre, edition, publisher, sell_price, buy_price)
        try:
            self.authorManager.add_book(author, book)
        except:
            self.authorManager.add(author, None)
            self.authorManager.add_book(author, book)

    def modify_book(self, book_title, attr, value):
        self.bookManager.modify(book_title, attr, value)

    def remove_book(self, book_title):
        book = self.bookManager.remove(book_title)
        self.remove_book_from_author(book.get_author(), book_title)

    # Order methods

    def add_order(self, client_name, qtd, price):
        self.orderManager.add(client_name, qtd, price)

    def check_order(self, client_name):
        self.orderManager.get_info(client_name)

    def modify_order(self, client_name, attr, value):
        self.orderManager.modify(client_name, attr, value)

    def remove_order(self, client_name):
        self.orderManager.remove(client_name)
