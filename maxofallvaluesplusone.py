"""
Define new functions using @qgsfunction. feature and parent must always be the
last args. Use args=-1 to pass a list of values as arguments
"""

from qgis.core import *
from qgis.gui import *
from qgis.utils import *

@qgsfunction(args=0, group='Custom')
def maxofallvaluesplusone(value1, feature, parent):
	layer=iface.activeLayer()
	return layer.maximumValue(layer.fieldNameIndex('fid')) + 1
