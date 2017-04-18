from qgis.core import *
from qgis.gui import *

"""
Example: concat("name", ', ', "iso_a2", ': ', label_pop_growth() )
"""
@qgsfunction(args=0, group='Custom_label')
def label_pop_growth(value1, feature, parent):
	name = feature['name']
	country_code = feature['iso_a2']
	pop_max = feature['pop_max']
	pop_min = feature['pop_min']
	pop_growth = float(pop_max)/pop_min
	return "{0:.2f}".format(pop_growth)


"""
Example: concat("name", ', ', "iso_a2", ', ', label_hemisphere() )
"""
@qgsfunction(args=0, group='Custom_label')
def label_hemisphere(value1, feature, parent):
	name = feature['name']
	country_code = feature['iso_a2']
	if feature['latitude'] > 0:
		hemisphere = 'N'
	else:
		hemisphere = 'S'
	return hemisphere
