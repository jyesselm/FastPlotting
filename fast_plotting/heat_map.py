#!/usr/bin/python 

import argparse
import random
import re
import sys

import numpy.random
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors


from file_io import *

def parse_args():
	parser = argparse.ArgumentParser(description='')

	parser.add_argument('-f',help='Data file path',required=True)
	parser.add_argument('-l',required=False)
	parser.add_argument('--test',required=False)

	parser.add_argument('--options', '-o', action="store",required=False)
	args = parser.parse_args()
	return args

def points_to_heatmap(x,y,weights=None,bins=10):
	if not weights:
		heatmap,xedges,yedges = np.histogram2d(x,y, bins=bins)
	else:
		heatmap,xedges,yedges = np.histogram2d(x,y, weights=weights,normed=True, bins=bins)

	x_axis_str = ["%.2f" % round(a,2) for a in xedges[:-1]]
	y_axis_str = ["%.2f" % round(a,2) for a in yedges[:-1]]

	return heatmap,x_axis_str,y_axis_str

		
class FPHeatMap(object):
	def __init__(self,fig_index=1,**options):
		self.get_default_options()
		self.set_options(options)


		self.fig_index=fig_index
		self.map = None

	def setup(self,heatmap,x_axis,y_axis):
		
		fig = plt.figure(self.fig_index)
		self.ax = fig.add_subplot(111)
		self._set_plt_options()
		

		self.ax.imshow(heatmap,interpolation="nearest",aspect=1)
		self.ax.set_xticks(range(len(x_axis)))
		self.ax.set_yticks(range(len(y_axis)))
		self.ax.set_xticklabels(x_axis,rotation=90)
		self.ax.set_yticklabels(y_axis)

	def show(self,heatmap,x_axis,y_axis):

		self.setup(heatmap,x_axis,y_axis)
		plt.show()

	def get_default_options(self):
		self.options = {'xlabel': None, 
						'ylabel': None,
						'title' : None}

	def set_options(self,user_options):

		for v,k in user_options.iteritems():
			if v in self.options:
				self.options[v] = k

	def _set_plt_options(self):
		plt.rc("font", size=16)
		plt.rcParams['font.sans-serif']='HelveticaLight'
		plt.xlabel(self.options['xlabel'],fontsize=24)
		plt.ylabel(self.options['ylabel'],fontsize=24)
		plt.title(self.options['title'],fontsize=26)
		plt.gcf().subplots_adjust(bottom=0.20)

	def add_point(self,point):
		self.ax.plot([point[0]],[point[1]],marker='o',color='white',markersize=10)


def randtest():

	# Generate some test data
	x = np.random.randn(8873)
	y = np.random.randn(8873)
	
	heatmap,x_axis,y_axis = points_to_heatmap(x,y,bins=10)

	fig = plt.figure(1)
	plt.imshow(heatmap,interpolation="nearest",aspect=1)
	plt.xticks(range(len(x_axis)),x_axis,rotation=90)
	plt.yticks(range(len(y_axis)),y_axis)
	plt.show()
	sys.exit()

	fphm = 	FPHeatMap(1, x, y,xlabel="It's Random!")
	fphm.setup()
	fphm.show()

def randtest2():
	# Generate some test data
	x = np.random.randn(8873)
	y = np.random.randn(8873)
	
	heatmap,x_axis,y_axis = points_to_heatmap(x,y,bins=10)
	fphm = 	FPHeatMap(1,xlabel="It's Random!")
	fphm.show(heatmap,x_axis,y_axis)
	sys.exit()

	fphm = 	FPHeatMap(1, x, y,xlabel="It's Random!")
	fphm.setup()
	fphm.show()

def filetest():
	path = "/Users/jyesselm/projects/REDESIGN/lib/prediction/plot_1.dat"

	heatmap,x_axis,y_axis = parse_file_to_heatmap(path)

	fphm = 	FPHeatMap(xlabel="It's Random!")
	fphm.show(heatmap,x_axis,y_axis)



if __name__ == '__main__':
	randtest2()
	sys.exit()


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





















	