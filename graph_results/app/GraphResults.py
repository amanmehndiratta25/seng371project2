import mpld3
from matplotlib.pylab import *
import datetime
import os 
import sys
from HighlightLines import HighlightLines


def read_data(data):
	dates = []
	values = []
	values_avg = []
	
	for line in data:
		line = line.rstrip('\n').split()
		year = int(line[0].split('-')[-2])
		month = int(line[0].split('-')[-1])
		day = 1
		dates = dates + [datetime.datetime(year, month, day)]
		values = values + [line[1]]
	values = [int(i) for i in values]
	scale = 100.0 / float(max(values))
	values = [float(i) * scale for i in values]
	for i in range(len(values)):
		values_avg = values_avg + [float((float(values[i]) + float(values[max(i-1, 0)]) + float(values[min(i+1, len(values) - 1)]))/3.0)]
	return dates, values, values_avg

def graph_results(datasets):
	use_avg = False
		
	if len(sys.argv) == 2:
		if sys.argv[1] == "-avg":
			print "using rolling average"
			use_avg = True

	x_array = []
	y_array = []
	label_array = []
	
	for label in datasets.keys():
		x, y, y_avg = read_data([s.strip() for s in datasets[label].splitlines()])
		if use_avg == True:
			y = y_avg
		x_array.append(x)
		y_array.append(y)
		label_array.append(label)
		
	# Draw lines
	fig = plt.figure(figsize=(13, 7), dpi=100) 
	plt.xlabel('Date')
	plt.ylabel('Percentage of maximum value')
	ax = fig.add_subplot(111)

	lines = []

	for i in range(len(x_array)):
		line = ax.plot(x_array[i], y_array[i], label=label_array[i], lw=5, alpha=0.4)
		mpld3.plugins.connect(fig, HighlightLines(line))

	min_date = datetime.datetime(2008, 1, 1)
	max_date = datetime.datetime(2015, 1, 1)
		
	ax.plot([min_date, max_date], [100,100], label="100% of maximum value", lw=2, color='k')

	ax.set_yticks([], [])
	plt.ylim([0, 150])
	plt.xlim([min_date, max_date])

	ax.grid(color='lightgray', alpha=0.7)
	ax.legend(loc='upper center', title="", framealpha=0.4)

	html = mpld3.fig_to_html(fig)

	return html
