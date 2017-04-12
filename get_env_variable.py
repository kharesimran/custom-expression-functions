from qgis.core import *
from qgis.gui import *
from qgis.utils import *

@qgsfunction(args='auto', group='Custom')
def env(var_name, feature, parent):
	""" Returns the value of the variable 'var_name' 
		Example usage: env('user_full_name') """
	
	active_layer = iface.activeLayer()
	
	if QgsExpressionContextScope.hasVariable(QgsExpressionContextUtils.layerScope(active_layer), var_name):
		return QgsExpressionContextScope.variable(QgsExpressionContextUtils.layerScope(active_layer), var_name)
		
	elif QgsExpressionContextScope.hasVariable(QgsExpressionContextUtils.projectScope(), var_name):
		return QgsExpressionContextScope.variable(QgsExpressionContextUtils.projectScope(), var_name)
	
	elif QgsExpressionContextScope.hasVariable(QgsExpressionContextUtils.globalScope(), var_name):
		return QgsExpressionContextScope.variable(QgsExpressionContextUtils.globalScope(), var_name)
	
	else:
		return ""
