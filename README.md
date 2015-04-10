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
1) Research Stack Exchange and Reddit APIs

2) Write a python script to utilize the APIs to search for mentions of certain projects by date using these APIs

3) Run git log on the codebases to get the number of contributors per month

4) Run git log on the codebases to get the number of commits per month

5) Compare project size with social media information. Use matplotlib to graph the outputs together and see if there is any correlation. Make graphs look super cool.

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

Installing Dependencies
-----

This section assumes you are going to use pip to install the python modules. Something else like easy_install would almost definitely work as well, but it hasn't been tested. 

It is strongly suggested that you do everything in the following order, as the requests module can be a real pain to update.

*make sure pip is up to date*
- if you don't already have pip installed, use this installer: 
	https://bootstrap.pypa.io/get-pip.py

*upgrade requests*
- if you don't upgrade requests, bad things will happen when you try the next few steps. 
- now you can install the extras to prevent the annoying InsecurePlatformWarning warnings
- if you get to this step without any problems, the rest should be easy.
- if you see something like this, you'll have to reinstall pip and try again.

*install praw*
- install the latest version
-  if you didn't follow the previous steps and install praw with an old version of pip such as 1.5.4, it will try to update requests and destroy pip.

*install flask*
- install the latest version

*install matplotlib*
- good luck doing this without running into problems
- the best way is to just get a python distribution with matplotlib included, but if you don't have such a version....
- on linux, I was able to just do this:
- if you try doing that and you get an error about freetype, see here http://stackoverflow.com/questions/9829175/pip-install-matplotlib-error-with-virtualenv

*install Tkinter*
- if you have a python distribution with matplotlib included, or depending on how you installed matplotlib, Tkinter might also be included already
- you can always run the check_dependencies.py script and see if it tells you you need Tkinter.
- on linux, this works:

*install mpld3*
- install the latest version














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

![Bootstrap](http://i.imgur.com/8SUoNgH.png)
![Angular](http://i.imgur.com/Wv33fk1.png)
![Rails](http://i.imgur.com/nWQXc4t.png)

- Analysis

- Answer to question

- Threats to Validity

- Future Work

Demo
-----
[LINK](https://www.youtube.com/watch?v=DWoOsjzO2A4)
