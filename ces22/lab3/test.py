from factory import WeddingCakeFactory, BirthdayCakeFactory, InformalCakeFactory
from builder import CakeBuilder

builder = CakeBuilder()
factory = WeddingCakeFactory()

chocCakeWeddFact = factory.createChocolateCake()

builder.buildStyle('wedding')
builder.buildFlavor('chocolate')

chocCakeWeddBuild = builder.getResult()

if (chocCakeWeddBuild.flavor == chocCakeWeddFact.flavor and chocCakeWeddBuild.style == chocCakeWeddFact.style):
      print('Cakes are equal')
else:
      print('Cakes are different')