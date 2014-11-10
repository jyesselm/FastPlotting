

import random
import numpy as np 

from   plot_types  import *
from   plot_base   import *

class HeatMapData(object):
	def __init__(self,options,heatmap,x_axis,y_axis):
		self.options = options
		self.heatmap = heatmap
		self.x_axis  = x_axis
		self.y_axis  = y_axis
		self.type    = PlotType.HEATMAP

def HeatMapOptions():
	options = {

	}

	for k,v in BaseOptions().iteritems(): options[k]=v
	return options


def points_to_heatmap(points,weights=None,bins=10):

	x = [] 
	y = []
	for p in points:
		x.append(p[0])
		y.append(p[1])
	x = np.array(x)
	y = np.array(y)

	if not weights:
		heatmap,xedges,yedges = np.histogram2d(x,y, bins=bins)
	else:
		heatmap,xedges,yedges = np.histogram2d(x,y, weights=weights,normed=True, bins=bins)

	x_axis_str = ["%.2f" % round(a,2) for a in xedges[:-1]]
	y_axis_str = ["%.2f" % round(a,2) for a in yedges[:-1]]

	return heatmap,x_axis_str,y_axis_str


