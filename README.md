# seng371project2

Colin Knowles (@knowlesc) and Ryan McDonald (@ryanmcdonald)

Question
-------
Does the activity on Stack Overflow, or social media sites such as Twitter, drive the number of contributors/size of a project or does actually contributing to the project tend to drive users to use social media? 

**Hypotheses**: We think that the number of contributors/project size should drive the mentions on social media. We think that in order to gain a "foothold" on social media-type sites, a project would need a certain number of contributors, so we will see the contributors increase dramatically before we see social media mentions start to increase. After this initial activity..... who knows what will happen.

Datasets
-------
**Codebases**: [Angular](https://github.com/angular/angular.js), [Bootstrap](https://github.com/twbs/bootstrap), and [Rails](https://github.com/rails/rails)

**APIs**: [Stack Exchange API](https://api.stackexchange.com), [Reddit API](http://www.reddit.com/dev/api)

**Metrics**:
To answer our project question, we needed two compare two categories of projects: Project Size vs Social Media Activity. Using these two sets of metrics we can try to determine whether or not there is a correlation.

- Project Size
  - Number of contributors per month
  - Number of commits per month
- Social Media Activity
  - Number of posts for each month in the Subreddits for each project
  - Number of Stack Overflow questions asked in a weekly period of each month that are tagged with the appropriate project tag

Methodology
--------
1) Research Stack Exchange and Reddit API's

2) Write a python script to utilize the API's to search for mentions of certain projects by date using these APIs

3) Run git log on the codebases to get the number of contributors per month

4) Run git log on the codebases to get the number of commits per month

5) Compare project size with social media information. Use matplotlib to graph the outputs together and see if there is any correlation.

Milestones (Revised March 24, 2015)
-----------------------------------
|#|Milestone|Date|Assignee|Status|
|----|---------|----|------------|------|
|1|**Research Stack Exchange API**|Mar. 13|Ryan|Completed|
|2|**Create Python program to automatically retrieve a count of mentions of a certain project from Stack Exchange API**|Mar. 17|Colin|Completed|
|3|**Create Python program to automatically run git log and get the data we need from a repository (# of contributors, project size)**|Mar. 17|Ryan|Completed|
|4|**Create Python program to automatically retrieve a count of mentions of a certain project from Reddit API**|Mar. 24|Colin|In progress|
|5|**Create Python program to run the previous three programs and graph their outputted data**|Mar. 30|Everyone|Completed|
|6|**Perform analysis on graphs**|Apr. 1|Everyone|In progress|

Tools
-----
our python scripts - todo
required libraries: pip:
	wget https://raw.github.com/pypa/pip/master/contrib/get-pip.py
	python get-pip.py 
	(if pip is not installed this way, there may be a conflict installing requests [https://bugs.launchpad.net/ubuntu/+source/python-pip/+bug/1306991] and you will have to reinstall pip this way to fix it)
reddit: 
	praw (sudo pip install praw)
	notes: nonexistent subreddit will cause error
stack: 
	requests (sudo pip install requests[security]) (security is needed)
	may need to put the api key in quotes if it's failing
graph:
	batch script for windows, otherwise python run.py
	Flask (sudo pip install flask)
	mpld3 (sudo pip install mpld3)
	matplotlib (sometimes comes with python, can be found online easily) (sudo pip install python-matplotlib)
		if this doens't work, try (sudo apt-get install python-matplotlib)
		may also need to do (sudo apt-get install python-tk if it still complains)


(need instructions too)

Results
-----
- Analysis

- Answer to question

- Threats to Validity

- Future Work

Demo
-----
a link to a video screencast demonstrating your work!
