#	utils.py
#
#	Author: Jason Bolden
#	
#	Date: 05/16/2013
#	
#	Description: This module contains all utility functions
#	and objects used in this application. All utitlity functions
#	should and must be unit tested.

conversionFactors = {
	'unit_m':{
		'g':1.,
		'kg':1000.
	},
	'unit_v':{
		'ml':.00422675,
		'l':4.22675,
		'c':1.,
		'tbsp':1./16,
		'tsp':1./48,
		'oz':1./8,
		'pt':2.,
		'q':4.,
		'gal':16.
	},
	'unit_w':{
		'oz':1./16,
		'lb':1.
	},
	'unit_c':{
		'u':1.
	}
}

def toUnits(quantity, unit):
	base_unit = ""
	for base in conversionFactors:
		if unit in conversionFactors[base]:
			base_unit = base
			break
	return quantity*conversionFactors[base_unit][unit]
