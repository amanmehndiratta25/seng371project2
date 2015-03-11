import sys
import requests 
import time
import datetime
'''
print "Enter tag to search for: "
tag = raw_input(">> ")

'''
do_query = False

months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
years = [2012, 2013, 2014]
days = [1, 2]
count = 0

			

date2 = datetime.datetime(2015, 3, 1, 0, 0, 0, 0, None)
utc_seconds = int(time.mktime(date2.timetuple()))
print datetime.datetime.fromtimestamp(utc_seconds)

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
	
if do_query:
	print "performing query" 
	query = base + page + pagesize + fromdate + todate + order + sort + tagged + site
	print query
	print '\n'

	r = requests.get(query)
	if r.json()['has_more'] == False:
		count = len(r.json()['items'])
	
	f = open("test.txt", "w")
	f.write(str(r.json()))
	
def main():
	if len(sys.argv) == 2:
		tag = str(sys.argv[1])
	else:
		print "Enter tag to search for: "
		tag = str(raw_input(">> "))
	
	dates = get_dates(tag)
	
	for date in dates:
		print make_query(1, date[1], date[2], tag)
	
if __name__ == "__main__":
	main()
