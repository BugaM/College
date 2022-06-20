from Pizza import *

# The classic
margherita = Tomato(Cheese(Basil(Box())))
print(margherita.getDescription() + ": $" + str(margherita.getTotalCost()))
# House's special
chocolateBacon = Bacon(Chocolate(Box()))
print(chocolateBacon.getDescription() + ": $" + str(chocolateBacon.getTotalCost()))