

class Recipe:
	def __init__(self, time: float, materials: tuple, products: tuple):
		self.T = time
		self.products = args[0:-1]
		self.educts = args[-1]
	def __str__(self):
		print(f"Educts: {materials}, products: {products}")



class Item:
	def __init__(self, name: str, isMaterial=False: bool):
		self.name = name
		self.isMaterial = isMaterial
		#self.recipe = recipe
	def add_recipe(self, recipe):
		self.recipe = recipe
		print(recipe)



gear = Item("Gear")
