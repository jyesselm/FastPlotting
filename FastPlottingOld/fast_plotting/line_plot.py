#!/usr/bin/python 

import argparse
import random
import re
import sys

import numpy as np
import matplotlib.pyplot as plt

from file_io import *

def parse_args():
	parser = argparse.ArgumentParser(description='')

	parser.add_argument('-f',help='Data file path',required=True)
	parser.add_argument('-l',required=False)

	parser.add_argument('--options', '-o', action="store",required=False)
	args = parser.parse_args()
	return args


class FPLinePlot(object):
	def __init__(self,fig_index,x,y,**options):
		self.get_default_options()
		self.set_options(options)

		self.fig_index = fig_index
		self.x = x
		self.y = y

	def plot(self):

		fig = plt.figure(self.fig_index)
		plt.rc("font", size=16)
		plt.rcParams['font.sans-serif']='Arial'


		xmin,xmax = self.buffer_bounds(self.x)
		ymin,ymax = self.buffer_bounds(self.y)

		plt.xlabel(self.options['xlabel'],fontsize=18)
		plt.ylabel(self.options['ylabel'],fontsize=18)
		plt.title(self.options['title'],fontsize=20)

		plt.xlim([xmin,xmax])
		plt.ylim([ymin,ymax])
		plt.plot(self.x,self.y,marker='o',color='black',markersize=9,linewidth=1.5)
		plt.show(self.fig_index)

	def get_default_options(self):
		self.options = {'xlabel': "Xlabel", 
						'ylabel': "Ylabel",
						'title' : "Title"}

	def set_options(self,user_options):

		for v,k in user_options.iteritems():
			if v in self.options:
				self.options[v] = k

	def buffer_bounds(self,data):
		dmin = 1000
		dmax = -1000

		for p in data:
			if p > dmax:
				dmax = p
			if p < dmin:
				dmin = p
		drange = abs(dmax - dmin)


		return dmin-drange*0.05,dmax+drange*0.05

def test():
	x1 = np.linspace(0, 10, 20)
	y1 = np.sin(x1)
	fig = plt.figure()
	FPLinePlot(1, x1, y1)

def randtest():
	x = []
	y = []
	size = 100

	for i in range(size):
		rand_x = random.randrange(-100,100)
		rand_y = random.randrange(-100,100)
		x.append(rand_x)
		y.append(rand_y)
	
	x.sort()


	fplp = 	FPLinePlot(1, x, y,xlabel="It's Random!")
	fplp.plot()

def lineartest():
	x = []
	y = []
	size = 100

	for i in range(size):
		rand_x = random.randrange(-100,100)
		rand_y = random.randrange(-100,100)
		x.append(rand_x)
		y.append(rand_y)
	
	x.sort()
	y.sort()

	fplp = 	FPLinePlot(1, x, y,xlabel="It's Random!")
	fplp.plot()

def get_random_file():
	pass



if __name__ == '__main__':

	args = parse_args()
	data = []
	x = []
	y = []
	options = {}
	if args.f:
		data = parse_file_to_2D_array(args.f)
		lanes = args.l
		if not lanes:
			lanes = "0,1"
		x,y = get_x_and_y_from_data(data, lanes)

	if args.options:
		options = parse_options(args.options)


	fplp = FPLinePlot(1, x, y)
	fplp.set_options(options)
	fplp.plot()





















	