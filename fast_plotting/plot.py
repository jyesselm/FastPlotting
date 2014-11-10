

import numpy as np 
import matplotlib.pyplot as plt

from   plot_types    import *
from   heat_map_plot import *


class Plot(object):
	def __init__(self,index=111):
		self.pindex = 0
		self.ax = plt.subplot(index,aspect='equal')
		self.datas = []

	def add_heatmap(self,points=None,weights=None,heatmap=None,x_axis=None,y_axis=None,**options):
		if points != None:
			heatmap,x_axis,y_axis = points_to_heatmap(points,weights)

		options = HeatMapOptions()
		data = HeatMapData(options,heatmap,x_axis,y_axis)
		self.datas.append(data)

	def add_scatter(self):
		pass

	def plot_data(self):
		for d in self.datas:
			if d.type == PlotType.HEATMAP: self.plot_heatmap(d)


	def plot_heatmap(self,data):
		plt.rc("font", size=16)
		self.ax.imshow(data.heatmap,interpolation="nearest")
		self.ax.set_xticks(range(len(data.x_axis)))
		self.ax.set_yticks(range(len(data.y_axis)))
		self.ax.set_xticklabels(data.x_axis,rotation=90)
		self.ax.set_yticklabels(data.y_axis)
		#self.ax.set_xlabel("Test",fontsize=24)


	def show(self):
		self.plot_data()
		plt.tight_layout()
		plt.show()


def test():
	points = np.random.random_sample((1000,2))	

	plot = Plot()
	plot.add_heatmap(points)
	plot.show()


if __name__ == '__main__':
	test()