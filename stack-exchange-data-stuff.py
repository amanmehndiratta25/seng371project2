import sys
import requests 
import time
import datetime
import os.path

'''
	Need numpy http://www.lfd.uci.edu/~gohlke/pythonlibs/#numpy
	Need matplotlib, requests 
	Might also need this: http://aka.ms/vcpython27
'''

do_query = False

months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
years = [2008, 2009, 2010, 2011, 2012, 2013, 2014]
days = [1, 2]

'''
	Returns a list of tuples, each containing a "title", and a start/end time
	Each tuple is used to provide the start and end times for each query
	The title is used to check if this query has been done before (to save API calls)
'''
def get_dates(tag):
	dates = []
	for year in years:
		for month in months:
			title = tag + "-" + str(year) + "-" + str(month) 
			date1 = datetime.datetime(year, month, days[0], 0, 0, 0, 0, None)
			date2 = datetime.datetime(year, month, days[1], 0, 0, 0, 0, None)
			utc_seconds1 = int(time.mktime(date1.timetuple()))
			utc_seconds2 = int(time.mktime(date2.timetuple()))
			dates.append((title, utc_seconds1, utc_seconds2))
	return dates

'''
	Creates an API call based on a tag to search for, a page, and a date range (it doesn't actually perform the call)
	Page should be 1 for the first call, then increased for the next call if "has_more" in the returned json is true, 
'''
def make_query(page_value, from_value, to_value, tag):
	base = "https://api.stackexchange.com/2.2/search?"
	page = "page=" + str(page_value)
	pagesize = "&pagesize=100"
	fromdate = "&fromdate=" + str(from_value)
	todate = "&todate=" + str(to_value)
	order = "&order=desc"
	sort = "&sort=activity"
	tagged = "&tagged=" + str(tag)
	site = "&site=stackoverflow"
	query = base + page + pagesize + fromdate + todate + order + sort + tagged + site
	return query
	
'''
	check existing file to see what queries have already been done
'''
def read_existing(output_file):
	tags = {}
	if os.path.isfile(output_file):
		f = open(output_file, 'r')
		for line in f:
			line = line.rstrip('\n').split()
			tags[line[0]] = line[1]
		print "Found existing file " + output_file
		f.close()
	return tags
		
def main():
	if len(sys.argv) == 2:
		tag = str(sys.argv[1])
	else:
		print "Enter tag to search for: "
		tag = str(raw_input(">> "))
		
	output_file = tag + "-api-counts.txt"

	tags = read_existing(output_file)

	f = open(output_file, 'w')
	dates = get_dates(tag)
	
	for date in dates:
		page = 1
		count = 0
		has_more = True
		
		# Only perform a query if it has not already been done
		
		if (date[0] not in tags.keys()):
			while has_more == True:
				
				query = make_query(page, date[1], date[2], tag)
				r = requests.get(query)
				
				has_more = r.json()['has_more']
				count = count + len(r.json()['items'])
				page = page + 1
				
				quota_remaining = str(r.json()['quota_remaining'])
				print quota_remaining + " API calls remaining"
				if quota_remaining == 0:
					print "No API calls remaining, exiting program."
					sys.exit()
			towrite = date[0] + " " + str(count)
			print "New data point " + towrite
			f.write(towrite + "\n")
		else:
			towrite = date[0] + " " + str(tags[date[0]])
			print "Already found data point " + towrite
			f.write(towrite + "\n")
	
if __name__ == "__main__":
	main()
