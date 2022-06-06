from abc import ABC, abstractmethod


class Person(ABC):
    '''
    Abstract class for persons
    '''

    def __init__(self):
        pass

    @abstractmethod
    def modify(self, attr, value):
        pass


class Client(Person):
    '''
    Bookstore client class
    '''

    def __init__(self, cpf, name, email):
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


class Author(Person):
    '''
    Book author class
    '''

    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def get_name(self):
        return self.name

    def get_books(self):
        return self.books

    def modify(self, attr, value):
        if attr == 'name':
            self.name = value
        elif attr == 'email':
            self.email = value
        else:
            print('Unrecognized attribute')

    def remove_book(self, title):
        for book in self.books:
            if book.get_title() == title:
                self.books.remove(book)
