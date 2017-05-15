from qgis.core import *
from qgis.gui import *

@qgsfunction(args='auto', group='Custom', usesgeometry=True)
def get_jitter_line(offset, feature, parent):
	geom = feature.geometry()
	line_length = geom.length()
	segment_length = 0.1*line_length
	point_distance = segment_length
	list_of_points = []
	while point_distance < line_length:
		point = geom.interpolate(segment_length).asPoint()
		point.set(point.x() + 10, point.y())
		list_of_points.append(point)
	jitter_line = QgsGeometry.fromPolyline(list_of_points)

def get_points_on_line(geom):
	""" Return an array of points along the line """

	line_length = geom.length()
	segment_length = 0.1*line_length
	point_distance = segment_length

	list_of_points = []
	while point_distance < line_length:
		point = geom.interpolate(point_distance)
		point_feature = QgsFeature()
		point_feature.setGeometry(point)
		list_of_points.append(point_feature)
		point_distance += segment_length
	return list_of_points
