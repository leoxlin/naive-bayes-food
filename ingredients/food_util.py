

def get_ingredient_count(foods):
	ingredient_dict={}
	for food in foods:
		ingredients=food.get_ingredient()

			# Iterate through all the ingredients
			for ingre in ingredients:
				if(ingre in ingredient_dict):
					ingredient_dict[ingre]+=1
				# If this ingredient has never been seen before
				# Initialize it to 1
				else
					ingredient_dict[ingre]=1
	return ingredient_dict;
