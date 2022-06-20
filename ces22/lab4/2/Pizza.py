class PizzaComponent:
      def getDescription(self):
            return self.__class__.__name__
      def getTotalCost(self):
            return self.__class__.cost

class Box(PizzaComponent):
      '''Pizza box'''
      cost = 0.25


class Decorator(PizzaComponent):
      def __init__(self, drinkComponent):
            self.component = drinkComponent
      def getTotalCost(self):
            return self.component.getTotalCost() + PizzaComponent.getTotalCost(self)
      def getDescription(self):
            return self.component.getDescription() + ' ' + PizzaComponent.getDescription(self)


class Pepperoni(Decorator):
      '''Pepperoni ingredient'''
      cost = 4.00
      def __init__(self, pizzaComponent):
            Decorator.__init__(self, pizzaComponent)

class Cheese(Decorator):
      '''Cheese ingredient'''
      cost = 3.00
      def __init__(self, pizzaComponent):
            Decorator.__init__(self, pizzaComponent)

class Bacon(Decorator):
      cost = 5.00
      def __init__(self, pizzaComponent):
            Decorator.__init__(self, pizzaComponent)

class Chocolate(Decorator):
      '''Chocolate ingredient'''
      cost = 5.00
      def __init__(self, pizzaComponent):
            Decorator.__init__(self, pizzaComponent)

class Basil(Decorator):
      '''Basil ingredient'''
      cost = 1.25
      def __init__(self, pizzaComponent):
            Decorator.__init__(self, pizzaComponent)

class Tomato(Decorator):
      cost = 1.50
      def __init__(self, pizzaComponent):
            Decorator.__init__(self, pizzaComponent)
