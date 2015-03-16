from pylab import *
import datetime
import os
import sys

def read_file(output_file):
  dates = []
  values = []
  if os.path.isfile(output_file):
    f = open(output_file, 'r')
    for line in f:
      line = line.rstrip('\n').split()
      year = int(line[0].split('-')[-3])
      month = int(line[0].split('-')[-2])
      day = int(line[0].split('-')[-1])

      print str(year) + "-" + str(month) + "-" + str(day)
      dates = dates + [datetime.datetime(year, month, day)]
      values = values + [line[1]]
    print "Found existing file " + output_file
    f.close()
  return dates, values

x, y = read_file(sys.argv[1])

plot(x, y)
show()
