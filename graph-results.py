from pylab import *
import datetime
import os 
import sys

def read_stack(output_file):
	dates = []
	values = []
	values_avg = []
	
	if os.path.isfile(output_file):
		f = open(output_file, 'r')
		for line in f:
			line = line.rstrip('\n').split()
			year = int(line[0].split('-')[-2])
			month = int(line[0].split('-')[-1])
			day = 1
			dates = dates + [datetime.datetime(year, month, day)]
			values = values + [line[1]]
		print "Found existing file " + output_file
		f.close()
	values = [int(i) for i in values]
	scale = 100.0 / float(max(values))
	values = [float(i) * scale for i in values]
	for i in range(len(values)):
		values_avg = values_avg + [float((float(values[i]) + float(values[max(i-1, 0)]) + float(values[min(i+1, len(values) - 1)]))/3.0)]
	return dates, values_avg
	
def read_reddit(output_file):
	dates = []
	values = []
	values_avg = []
	
	if os.path.isfile(output_file):
		f = open(output_file, 'r')
		for line in f:
			line = line.rstrip('\n').split()
			year = int(line[0].split('-')[-2])
			month = int(line[0].split('-')[-1])
			day = 1
			dates = dates + [datetime.datetime(year, month, day)]
			values = values + [line[1]]
		print "Found existing file " + output_file
		f.close()
	values = [int(i) for i in values]
	scale = 100.0 / float(max(values))
	values = [float(i) * scale for i in values]
	for i in range(len(values)):
		values_avg = values_avg + [float((float(values[i]) + float(values[max(i-1, 0)]) + float(values[min(i+1, len(values) - 1)]))/3.0)]
	return dates, values_avg

def read_stats(output_file):
	dates = []
	values = []
	values_avg = []
	
	if os.path.isfile(output_file):
		f = open(output_file, 'r')
		for line in f:
			line = line.rstrip('\n').split()
			year = int(line[0].split('-')[-3])
			month = int(line[0].split('-')[-2])
			day = int(line[0].split('-')[-1])

			dates = dates + [datetime.datetime(year, month, day)]
			values = values + [line[1]]
		print "Found existing file " + output_file
		f.close()
	values = [int(i) for i in values]
	scale = 100.0 / float(max(values))
	values = [float(i) * scale for i in values]
	for i in range(len(values)):
		values_avg = values_avg + [float((float(values[i]) + float(values[max(i-1, 0)]) + float(values[min(i+1, len(values) - 1)]))/3.0)]
	return dates, values_avg

fig = plt.figure() 
fig.canvas.set_window_title('Rails') 
	
x, y = read_stats("gitlog_rails_data.txt")
plot(x, y, label="number of contributors")
x, y = read_stack("ruby-on-rails-stack-api-counts.txt")
plot(x, y, label="stack overflow questions created")
x, y = read_reddit("ruby-on-rails-reddit-data.txt")
plot(x, y, label="new reddit submissions")
plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3, ncol=3, mode="expand", borderaxespad=0.)

show()