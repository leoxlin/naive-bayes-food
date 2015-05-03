# An article of food available for consumption
class Food:

	# Contains:
	# Name/identifier of the food
	# Array of value for the ingredients used
	def __init__(self, name, ingredients=[]):
		self.name=name;
		self.ingredients=ingredients;

	# Append a nutritional value to the array of ingredients
	def add_ingredient(self, ingredient):
		self.ingredients.append(ingredient);

	# Return the ingredients of a food product
	def get_ingredient(self):
		return self.ingredients
