
import matplotlib.pyplot as plt
from pylab import rcParams

from   scatter_plot import *

class Plot(object):
	def __init__(self):
		self.subplots = []

	def add_subplot(self,subplot):
		self.subplots.append(subplot)

	def setup_orientation(self):
		if len(self.subplots) == 2:
			self.subplots[0].setup(121)
			self.subplots[1].setup(122)
		if len(self.subplots) == 3:
			self.subplots[0].setup(131)
			self.subplots[1].setup(132)
			self.subplots[2].setup(133)
		if len(self.subplots) == 4:
			self.subplots[0].setup(221)
			self.subplots[1].setup(222)
			self.subplots[2].setup(223)
			self.subplots[3].setup(224)

	def show(self):

		self.setup_orientation()

		for subplot in self.subplots:
			subplot.plot_data()

		plt.show()


def test():
	#rcParams['figure.figsize'] = 11, 3.4
	plot = Plot()
	plot.add_subplot(get_rand_scatter_plot())
	plot.add_subplot(get_rand_scatter_plot())
	plot.add_subplot(get_rand_scatter_plot())
	plot.show()

if __name__ == '__main__':
	test()
