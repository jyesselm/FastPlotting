
import matplotlib.pyplot as plt

from heat_map import *

class Plots(object):
	def __init__(self):
		self.plots = []
		self.count = 1

	def add_plot(self,plot):
		self.plots.append(plot)
		self.count += 1

	def new_heatmap(self,heatmap,x_axis,y_axis,**options):
		fphm = FPHeatMap(self.count)
		fphm.set_options(options)
		fphm.setup(heatmap,x_axis,y_axis)

		#if self.count > 1:
		#	thismanager = plt.get_current_fig_manager()
		#	thismanager.window.SetPosition((500, 0))

		self.plots.append(fphm)
		self.count += 1
		return fphm


	def show(self):
		plt.show()

