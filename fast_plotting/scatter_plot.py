#!/usr/bin/env python


import numpy as np
import matplotlib.pyplot as plt

class ScatterPlot(object):
	def __init__(self):
		self.pindex = 0
		self.ax = plt.subplot()
		self.options = self._get_default_options()

	#def setup(self):
	#	self.ax = plt.subplot()
	def plot(self,points):
		x = [] 
		y = []
		for p in points:
			x.append(p[0])
			y.append(p[1])
		x = np.array(x)
		y = np.array(y)

		self.ax.scatter(x,y,s=100,c=self.options['colors'][self.pindex],alpha=0.8)
		self.pindex += 1

	def show(self):
		plt.show()

	#private functions
	###########################################################################
	def _get_default_options(self):
		options = {
			'colors' : ['black','red','blue','green','orange']
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



def main():
	pass

if __name__ == '__main__':
	test()