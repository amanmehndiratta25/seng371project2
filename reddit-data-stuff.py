import praw
import datetime

output_file = "reddit-data.txt"

reddit = praw.Reddit(user_agent='rails_test_script')
posts = reddit.get_subreddit('rubyonrails').get_new(limit=None)

f = open(output_file, 'w')

dates = {}

for x in posts:
	dt = datetime.datetime.fromtimestamp(int(x.created_utc))
	date = str(dt.timetuple()[0]).zfill(2) + "-" + str(dt.timetuple()[1]).zfill(2)# + "-" + str(dt.timetuple()[2])
	if date in dates.keys():
		dates[date] = dates[date] + 1
	else:
		dates[date] = 1

for date in sorted(dates.keys()):
	dates[date] = dates[date]
	towrite = str(date) + " " + str(dates[date]) + "\n"
	f.write(towrite)
	
	
			
