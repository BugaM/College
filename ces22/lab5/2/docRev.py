from abc import ABC, abstractmethod



class State(ABC):
    """
    Class that represents document's states
    """
    def __init__(self, document):
        self.document = document

    @abstractmethod
    def render(self):
        """
        Renders document.
        """
        pass

    @abstractmethod
    def publish(self):
        """
        Publishes document.
        """
        pass

class Document:
    """
    Document class
    """
    def __init__(self, text, user):
        self.text = text
        self.user = user
        self.state = Draft(self)
    
    def render(self):
        """
        Render document in current state
        """
        self.state.render()
    
    def publish(self):
        """
        Publish document in current state
        """
        self.state.publish()
    
    def change_state(self, state):
        """
        Changes document's state
        """
        self.state = state


class Draft(State):
    """
    Draft state
    """
    def __init__(self, document):
        super().__init__(document)

    def render(self):
        if self.document.user.isAdmin or self.document.user.isAuthor:
            print("Rendering draft:")
            print(self.document.text)
        else:
            print("Error: rendering not authorized")

    def publish(self):
        if self.document.user.isAdmin:
            print('Publishing document')
            self.document.change_state(Published(self.document))
        else:
            self.document.change_state(Moderation(self.document))


class Moderation(State):
    """
    Moderation state
    """
    def __init__(self, document : Document) -> None:
        super().__init__(document)

    def render(self):
        if self.document.user.isAdmin or self.document.user.isAuthor:
            print("Rendering moderation:")
            print(self.document.text)
        else:
            print("Error: rendering not authorized")

    def publish(self):
        if self.document.user.isAdmin:
            print('Publishing document')
            self.document.change_state(Published(self.document))
        else:
            self.document.change_state(Draft(self.document))


class Published(State):
    """
    Published state
    """
    def __init__(self, document : Document) -> None:
        super().__init__(document)

    def render(self):
        print("Rendering published document:")
        print(self.document.text)

    def publish(self):
        print("Document already published")


class User:
    """
    Document user.
    """
    def __init__(self, isAdmin=False, isAuthor=False):
        self.isAdmin = isAdmin
        self.isAuthor = isAuthor


if __name__ == "__main__":

    employee = User()
    admin = User(isAdmin=True)
    author = User(isAuthor=True)

    text = "Life is beautiful"
    employee_doc = Document(text, employee)

    print("Employee document:")
    employee_doc.render()

    text = "When the sun goes down"
    author_doc = Document(text, author)

    print('Author document')
    author_doc.render()
    author_doc.publish()