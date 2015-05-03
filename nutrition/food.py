# An article of food available for consumption
class Food:

	# Contains:
	# Name/identifier of the food
	# Array of tuple value for the nutrition
	def __init__(self, name, nutrition=[]):
		self.name=name;
		self.nutrition=nutrition;

	# Append a nutritional value to the array of nutritions
	# Nutrition is a tuple:
	# (name of the nutrition[string], quantity[double])
	def add_nutrition(self, nutrition):
		self.nutrition.append(nutrition);

	# Return the nutritional value of a food product
	def get_nutrition(self):
		return self.nutrition
