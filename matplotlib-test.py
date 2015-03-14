from pylab import *
import datetime
import os 

def read_existing(output_file):
	dates = []
	values = []
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
	return dates, values
	
x, y = read_existing("ruby-on-rails-api-counts.txt")

	


plot(x, y)
show()