def who_am_I(func):
    def func_wrapper(*args, **kwargs):
        return "My name is {0[0]} and I am {0[1]} years old".format(func(*args, **kwargs))
    return func_wrapper


class Person(object):
    def __init__(self):
        self.name = "Marcelo"
        self.family = "Buga"
        self.age = 21

    @who_am_I
    def get_fullname_and_age(self):
        return self.name+" "+self.family, self.age


marcelo = Person()

print(marcelo.get_fullname_and_age())
