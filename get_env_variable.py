from qgis.core import *
from qgis.gui import *
from qgis.utils import *

@qgsfunction(args='auto', group='Custom')
def env(var_name, feature, parent):
    """ Returns the value of the variable 'var_name' 
        Example usage: env('user_full_name') """
    active_layer = iface.activeLayer()
    return QgsExpressionContextUtils.layerScope(active_layer).variable(var_name) \
         or QgsExpressionContextUtils.projectScope().variable(var_name) \
         or QgsExpressionContextUtils.globalScope().variable(var_name)
