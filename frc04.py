
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



class Item(Material):
	def __init__(self, name: str):
		self.name = name
		self.as_educt = []
		self.as_product = []
	def add_recipe_as_educt(recipe: Recipe):
		self.as_educt.append(recipe)
	def add_recipe_as_product(recipe: Recipe):
		self.as_product.append(recipe)

	def calculate()




class Recipe:
	def __init__(self, time: int, educts: dict, products: dict):
		self.time = time
		self.educts = educts		# educts = what comes in
		self.products = products	# products = what comes out


class Calculator:
