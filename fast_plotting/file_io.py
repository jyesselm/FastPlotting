
import numpy as np

def parse_options(options_str):
	p = re.compile(r'^\d')
	option_strs = options_str.split(",")
	options = {}
	for option_str in option_strs:
		spl = option_str.split("=")
		#check for boolean
		if len(spl) == 1:
			options[option_str] = 1
			continue
		if len(spl) > 2:
			raise ValueError("incorrect format for options: Option=Key, or simply Option each seperated by a comma")
		key,value = spl
		#is value a number
		if p.match(value):
			value = float(value)
		options[key] = value

	return options

def parse_file_to_2D_array(filename):
	f = open(filename)
	lines = f.readlines()
	f.close()

	data = [ x.split() for x in lines]
	return data

def get_x_and_y_from_data(data,lanes):
	xlane,ylane = parse_lanes(lanes)

	x = []
	y = []

	if not hasattr(xlane, '__call__'):
		for row in data:
			x.append(float(row[xlane]))
	if not hasattr(ylane, '__call__'):
		for row in data:
			y.append(float(row[ylane]))	

	if hasattr(xlane, '__call__'):	
		x = xlane(y)
	if hasattr(ylane, '__call__'):	
		y = ylane(x)



	return x,y

def parse_lanes(lanes):
	xlane,ylane = lanes.split(",")
	xlane = parse_lane(xlane)
	ylane = parse_lane(ylane)
	return xlane,ylane

def parse_lane(lane):
	p = re.compile(r'^\d+$')
	if p.match(lane):
		return int(lane)
	else:
		if lane == "c":
			return one_to_n

def one_to_n(other_lane):
	lane = []
	count = 0
	for n in other_lane:
		count += 1
		lane.append(count)

	return lane 

def parse_file_to_heatmap(filename):
	f = open(filename)
	lines = f.readlines()
	f.close()

	diff_max,diff_min,rot_diff_max,rot_diff_min,bins = [float(x) for x in lines.pop(0).split()]

	diff_incr = (diff_max - diff_min) / float(bins)
	rot_diff_incr = (rot_diff_max - rot_diff_min) / float(bins)

	xy = []

	for l in lines:
		row = [float(x) for x in l.split()]
		xy.append(row)
	xy = np.array(xy)

	x_axis = []
	y_axis = []

	for i in range(0,int(bins)):
		x_axis.append(diff_min)
		y_axis.append(rot_diff_min)

		diff_min += diff_incr
		rot_diff_min += rot_diff_incr


	x_axis_str = ["%.2f" % round(a,2) for a in x_axis]
	y_axis_str = ["%.2f" % round(a,2) for a in y_axis]

	return xy,x_axis_str,y_axis_str









