import sys
import requests 

'''
print "Enter tag to search for: "
tag = raw_input(">> ")

'''


fromdate_value = str(1425168000)
todate_value = str(1425254400)
tag = "ruby-on-rails"
page_value = str(1)

base = "https://api.stackexchange.com/2.2/search?"

page = "page=" + page_value
pagesize = "&pagesize=100"
fromdate = "&fromdate=" + fromdate_value
todate = "&todate=" + todate_value
order = "&order=desc"
sort = "&sort=activity"
tagged = "&tagged=" + tag
site = "&site=stackoverflow"

query = base + page + pagesize + fromdate + todate + order + sort + tagged + site
print query

r = requests.get(query)

f = open("test.txt", "w")
f.write(str(r.json()))
