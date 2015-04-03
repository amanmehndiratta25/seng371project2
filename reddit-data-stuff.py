import praw
import datetime
import sys 



def get_reddit_data(subreddit, output_file):
	agent = subreddit + "_python_post_count_script"
	reddit = praw.Reddit(user_agent=agent)
	posts = reddit.get_subreddit(subreddit).get_new(limit=None)

	
	f = open(output_file, 'w')

	dates = {}

	for x in posts:
		dt = datetime.datetime.fromtimestamp(int(x.created_utc))
		date = str(dt.timetuple()[0]).zfill(2) + "-" + str(dt.timetuple()[1]).zfill(2)
		if date in dates.keys():
			dates[date] = dates[date] + 1
		else:
			dates[date] = 1

	for date in sorted(dates.keys()):
		dates[date] = dates[date]
		towrite = str(date) + " " + str(dates[date]) + "\n"
		f.write(towrite)
	
	print "Data written to " + output_file
	
	
def main():
	subreddit = ""
	output_file = "reddit-data.txt"
	
	if len(sys.argv) == 2:
		subreddit = sys.argv[1]
	elif len(sys.argv) == 1:
		print "Enter subreddit name: "
		subreddit = str(raw_input(">> "))
	else:
		print "invalid argument"
		sys.exit()
		
	print "Getting data from subreddit: " + subreddit
	output_file = subreddit + "-" + output_file
	
	get_reddit_data(subreddit, output_file)
	
if __name__ == "__main__":
	main()