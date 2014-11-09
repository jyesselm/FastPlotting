#!/usr/bin/env python


import copy
import numpy as np
import matplotlib.pyplot as plt

class ScatterPlotData(object):
	def __init__(self,options,x,y):
		self.options = options
		self.x = x
		self.y = y

class ScatterPlot(object):
	def __init__(self,index=111):
		self.pindex = 0
		self.ax = plt.subplot(index,aspect='equal')
		self.options = self._get_default_options()
		self.colors = ['black','red','blue','green','orange']
		self.datas = []

	def setup(self,index):
		self.ax = plt.subplot(index,aspect='equal')

	def plot(self,points):
		x = [] 
		y = []
		for p in points:
			x.append(p[0])
			y.append(p[1])
		x = np.array(x)
		y = np.array(y)

		data = ScatterPlotData(copy.deepcopy(self.options), x, y)
		self.datas.append(data)

		
	def plot_data(self):
		for d in self.datas:
			self.ax.scatter(d.x,d.y,s=100,c=self.colors[self.pindex],alpha=0.8)
			self.pindex += 1

	def show(self):
		self.plot_data()
		plt.show()

	#private functions
	###########################################################################
	def _get_default_options(self):
		options = {
			'color' : None,
			'size'  : None,
			'xlabel': None, 
			'ylabel': None,
			'title' : None
		}
		return options


def test_no_class():
	#points = np.random.random_sample((100,2))
	x = np.random.random_sample(100)
	y = np.random.random_sample(100)

	ax = plt.subplot()
	ax.scatter(x,y,s=100,c='r')
	
	x = np.random.random_sample(100)
	y = np.random.random_sample(100)
	ax.scatter(x,y,s=100)

	plt.show()
	#sp = ScatterPlot()
	#sp.setup()

def test():
	points1 = np.random.random_sample((100,2))
	points2 = np.random.random_sample((100,2))
	points3 = np.random.random_sample((100,2))

	sp = ScatterPlot()
	sp.plot(points1)
	sp.plot(points2)
	sp.plot(points3)
	sp.show()

def test_multi():
	points1 = np.random.random_sample((100,2))
	points2 = np.random.random_sample((100,2))

	sp1 = ScatterPlot(121)
	sp2 = ScatterPlot(122)

	sp1.plot(points1)
	sp1.plot(points2)
	sp2.plot(points2)

	sp1.plot_data()
	sp2.plot_data()

	plt.show()

def get_rand_scatter_plot():
	points1 = np.random.random_sample((100,2))
	sp = ScatterPlot(111)
	sp.plot(points1)

	return sp


def main():
	pass

if __name__ == '__main__':
	test_multi()