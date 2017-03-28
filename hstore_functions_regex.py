from qgis.core import *
from qgis.gui import *
import re


"""
1. Given a key, return the value from hstore_attr
	If the key does not exist, return null
	Usage: hstore_get_value1('other_tags', 'tourism')
"""
@qgsfunction(args='auto', group='Custom1')
def hstore_get_value1(hstore_attr, key, feature, parent):
	
	hstore_string=feature[hstore_attr]
	regexp='"'+key+'"=>"(.+?)"'
	if hstore_string and re.search(regexp, hstore_string):
		return re.search(regexp, hstore_string).group(1)
	else:
		return ""


"""
2. Does the given key exist in hstore_attr? 
	Returns True or False
	Usage: hstore_exist1('other_tags', 'tourism')
"""
@qgsfunction(args='auto', group='Custom1')
def hstore_exist1(hstore_attr, key, feature, parent):

	hstore_string=feature[hstore_attr]
	regexp='"'+key+'"=>"(.+?)"'
	if hstore_string and re.search(regexp, hstore_string):
		return True
	else:
		return False


"""
3. Does key/value exist in hstore_attr?
	Returns True or False
	Usage: hstore_contains_key_value1('other_tags', '"tourism"=>"information"')
"""
@qgsfunction(args='auto', group='Custom1')
def hstore_contains_key_value1(hstore_attr, key_value, feature, parent):

	hstore_string=feature[hstore_attr]
	if hstore_string and re.search(key_value, hstore_string):
		return True
	else:
		return False


"""
5. Does hstore_attr contain hstore_string?
	Returns True or False
	Usage: 
	hstore_contains_hstore1('other_tags', '"tourism"=>"information","information"=>"guidepost"')
"""
@qgsfunction(args='auto', group='Custom1')
def hstore_contains_hstore1(hstore_attr, hstore_input_string, feature, parent):

	hstore_attr_string=feature[hstore_attr]
	if not hstore_attr_string:
		return False
	key_value_list=hstore_input_string.split(",")
	for key_value in key_value_list:
		if not re.search(key_value, hstore_attr_string):
			return False
	return True
