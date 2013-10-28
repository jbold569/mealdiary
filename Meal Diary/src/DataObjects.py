#	DataObjects.py
#
#	Author: Jason Bolden
#	
#	Date: 05/16/2013
#	
#	Description: This module contains all objects used
#	in this application. Objects are typically loaded
# 	and converted to dicts in order to interface with
#	mongodb.

import utils

# Class structure that will hold recipe information.
# This is used for deducting items from inventory and
# determining the amount of items needed to prepare
# the recipe.
class Recipe:
	def __init__(self, name='', ingredients={}, recipe_yield=0, directions=[], data=None):
		if data:
			self.__dict__ = data
		else:
			self.name = name
			# Structure {"name": quantity, ...}
			self.ingredients = ingredients
			self.recipe_yield = recipe_yield
			self.directions = directions
		
	def serialize(self):
		return self.__dict__
	
	def load(self, data):
		for key in self.__dict__:
			try:
				self.__dict__[key] = data[key]
			except KeyError:
				print "[ERROR] Loading Recipe: invalid data"
				return False

# Class structure that will hold item information.
# All item quantities are converted to base units.
# This is done to provide uniformity across items.
class Item:
	def __init__(self, name='', quantity=None, unit='', tags=[], data=None):
		if data:
			self.__dict__ = data
		else:	
			self.name = name
			self.quantity = utils.toUnits(quantity, unit)
			self.unit = unit
			self.tags = tags

	def serialize(self):		
		return self.__dict__


	def load(self, data):
		for key in self.__dict__:
			try:
				self.__dict__[key] = data[key]
			except KeyError:
				print "[ERROR] Loading Item: invalid data"
				return False
			
def test_code():
	items = []
	items.append(Item('whey protein', 1.5, 'u'))
	items.append(Item('frozen berries', .5, 'c'))
	items.append(Item('soy milk', 1, 'c'))
	items.append(Item('banana', 1, 'u'))
	items.append(Item('peanut butter', 1, 'tbsp'))

	ingredients = {
		'whey protein':(1.5, 'u'),
		'frozen berries':(.5, 'c'),
		'soy milk':(1, 'c'),
		'banana':(1, 'u'),
		'peanut buttter':(1,'tbsp')
	}
	directions = ['Combine in blender until smooth.']

	recipe = Recipe('Berry Protein Smoothie', ingredients, 1, directions)

	for item in items:
		print item.serialize()
	print "Recipe: ", recipe.serialize()
	
	cpy_recipe = Recipe(data=recipe.serialize())
	print "Cpy Recipe: ", cpy_recipe.ingredients

if __name__ == '__main__':
	test_code()
