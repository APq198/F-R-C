
from math import inf

print_output = True
rounding = 9

def print_style(depth, name, target, N_star=None):
	if not print_output: return
	s = "|  " * depth + f"{name}  ---  {round(target, rounding)}"
	if N_star is not None:
		s += f",  {round(N_star, rounding)}"
	print(s)



class Vector_for_materials:
	def __init__(self, key_init=None, val_init=None):
		self.d = dict()
		if key_init is not None:
			self.d.update({key_init: val_init})
			#print(self.d.keys())

	def __add__(self, other):	# self = self + other
		for key in other.d.keys():
			if key in self.d.keys():
				self.d[key] += other.d[key]
			else:
				self.d.update({key: other.d[key]})
		return self

	def __str__(self):
		s = ""
		for key in self.d.keys():
			s += f"{key.name} --- {round(self.d[key], rounding)}\n"
		return s





class Material:
	def __init__(self, name):
		self.name = name
		self.isMaterial = True
		#self.total_needed = 0

	def __str__(self):
		#return f"{self.name}: {round(self.total_needed, rounding)}"
		return self.name

	def calculate(self, target: float, depth: int = 0):
		#self.total_needed += target
		print_style(depth, self.name, target)
		return Vector_for_materials(self, target)



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
		print_style(depth, self.name, target, N_star)

		raw_materials = Vector_for_materials()
		for component_item in self.materials.keys():
			created_per_recipe_component = self.materials[component_item]
			component_target = target * ( created_per_recipe_component / self.created_per_recipe )
			raw_materials = raw_materials + component_item.calculate(component_target, depth+1)

		if depth == 0:
			print("\n\n" + str(raw_materials))
			return None

		return raw_materials


	def reverse_calculate(self, target):
		... 

### =================================================================== ###

# TODOs:
#	calculate in reverse


def plates_as_a_given():
	global iron_plate, copper_plate, steel, stone, stone_bricks
	iron_plate = Material("Iron Plate")
	copper_plate = Material("Copper Plate")
	steel = Material("Steel")
	stone = Material("Stone")
	stone_bricks = Material("Stone Bricks")

def basic_components():
	global gear, copper_cable, iron_rod
	gear_recipe = {iron_plate: 2}
	gear = Item("Gear", 0.5, 1, gear_recipe)
	copper_cable_r = {copper_plate: 1}
	copper_cable = Item("Copper Cable", 0.5, 2, copper_cable_r)
	iron_rod_r = {iron_plate: 2}
	iron_rod = Item("Iron Rod", 0.5, 2, iron_rod_r)

def green_circuit_recipe(given=True):
	global green_circuit
	if given:
		green_circuit = Material("Green Circuit")
	else:
		green_circuit_r = {copper_cable: 3, iron_plate: 1}
		green_circuit = Item("Green Circuit", 0.5, 1, green_circuit_r)

def basic_structures():
	global conv, inserter, furnace
	conv_r = {gear:1, iron_plate:1}
	conv = Item("Conveyor", 0.5, 2, conv_r)
	inserter_r = {green_circuit: 1, gear: 1, iron_plate: 1}
	inserter = Item("Inserter (basic)", 0.5, 1, inserter_r)
	furnace_r = {stone: 5}
	furnace = Item("Stone Furnace", 0.5, 1, furnace_r)

def science_packs():
	global red_science, green_science
	red_science_r = {copper_plate: 1, gear: 1}
	red_science = Item("Res Science", 5, 1, red_science_r)
	green_science_r = {inserter: 1, conv: 1}
	green_science = Item("Green Science", 6, 1, green_science_r)



if __name__ == "__main__":
	plates_as_a_given()
	basic_components()
	green_circuit_recipe(given = True)
	basic_structures()
	science_packs()
	green_science.calculate(15)
