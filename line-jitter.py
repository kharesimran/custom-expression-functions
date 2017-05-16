from qgis.core import *
from qgis.gui import *
from math import atan, sin, cos

@qgsfunction(args='auto', group='Custom', usesgeometry=True)
def get_jitter_line(offset, feature, parent):
	line = feature.geometry()
	length = line.length()
	point_distance = 0
	points_list = []
	while point_distance <= length:
		point = line.interpolate(point_distance).asPoint()
		points_list.append(point)
		point_distance += 0.1*length
	jitter_line = QgsGeometry.fromPolyline(get_displaced_points(points_list, offset))
	return jitter_line

def get_displaced_points(points_list, offset):
	a = math.atan((points_list[0].x() - points_list[-1].x())/(points_list[0].y() - points_list[-1].y()))
	# 'a' is the angle that the perpendicular to the line makes with the x axis 
	for point in points_list:
		point.set(point.x() + offset*sin(a) , point.y() + offset*cos(a))
	return points_list
