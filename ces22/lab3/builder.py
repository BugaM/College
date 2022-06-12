from cake import Cake
class CakeBuilder:
      def __init__(self):
            pass
      def buildStyle(self, style):
            self.style = style
      def buildFlavor(self, flavor):
            self.flavor = flavor
      def getResult(self):
            return Cake(self.style, self.flavor)