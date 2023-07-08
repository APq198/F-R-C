
from math import inf



def print_style(depth, name, target, N_star=None):
	s = " |  " * depth + f"{name}  ---  {target}"
	if N_star is not None:
		s += f",  {N_star}"
	print(s)



class Material:
	def __init__(self, name):
		self.name = name
		self.isMaterial = True
		self.total_needed = 0

	def __str__(self):
		print(f"{self.name}: {round(self.total_needed, 2)}")

	def calculate(self, target: float, depth: int = 0):
		self.total_needed += target
		#print(" |	" * depth + f"{self.name}  ---  {target}")
		print_style(depth, self.name, target)
		#return []



class Item(Material):
	def __init__(	self, 
					name: str,  
					time: float, 
					created_per_recipe: int, 
					materials: tuple
				):
		self.name = name
		self.time = time
		self.created_per_recipe = created_per_recipe
		self.materials = materials


	def calculate(self, target: float, depth: int = 0):

		N_star = target * self.time / self.created_per_recipe
		#print(" |  " * depth + f"{self.name}  ---  {target},  {N_star}")
		print_style(depth, self.name, target, N_star)

		for component in self.materials:
			created_per_recipe_component = component[0]
			item = component[1]
			component_target = target * ( created_per_recipe_component / self.created_per_recipe )
			raw_materials = item.calculate(component_target, depth+1)

iron_plate = Material("Iron Plate")

gear_recipe = [(2, iron_plate)]
gear = Item("Gear", 0.5, 1, gear_recipe)
#gear.calculate(1)
conv_recipe = [(1, iron_plate), (1, gear)]
conv = Item("Conveyor", 0.5, 2, conv_recipe)
conv.calculate(2)
