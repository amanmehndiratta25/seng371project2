# seng371project2

Colin Knowles (@knowlesc) and Ryan McDonald (@ryanmcdonald)

Question
-------
Does the activity on Stack Overflow, or social media sites such as Twitter, drive the number of contributors/size of a project or does actually contributing to the project tend to drive users to use social media? 

**Hypothesis**: We think that the number of contributors/project size should drive the mentions on social media. We think that in order to gain a "foothold" on social media-type sites, a project would need a certain number of contributors, so we will see the contributors increase dramatically before we see social media mentions start to increase. After this initial activity..... who knows what will happen.

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
|4|**Create Python program to automatically retrieve a count of mentions of a certain project from Reddit API**|Mar. 24|Colin|Completed|
|5|**Create Python program to run the previous three programs and graph their outputted data**|Mar. 30|Everyone|Completed|
|6|**Perform analysis on graphs**|Apr. 10|Everyone|Completed|

Installing Dependencies
-----

This section assumes you are going to use pip to install the python modules. Something else like easy_install would almost definitely work as well, but it hasn't been tested. It is strongly suggested that you do everything in the following order, as the requests module can be a real pain to update and will break older versions of pip really easily.

*make sure pip is up to date*
- If you don't already have pip installed, use this installer: 
	https://bootstrap.pypa.io/get-pip.py
![](http://i.imgur.com/MTm6Omv.png)

*upgrade requests*
- If you don't upgrade requests, bad things will happen when you try the next few steps. 
- ![](http://i.imgur.com/dXnZ3tt.png)
- Now you can install the extras to prevent the annoying InsecurePlatformWarning warnings.
- ![](http://i.imgur.com/K8fEvyJ.png)
- If you get to this step without any problems, the rest should be easy.
- If you start seeing something like this when you try to use pip, you'll have to reinstall pip and try again. It's a [known bug](https://bugs.launchpad.net/ubuntu/+source/python-pip/+bug/1306991).
- ![](http://i.imgur.com/ba7JJUu.png)

*install praw*
- Install the latest version.
- ![](http://i.imgur.com/bkfctYc.png)
- If you install praw with an old version of pip such as 1.5.4, it will try to update requests and destroy pip as in the screenshot above.

*install flask*
- Install the latest version.
- ![](http://i.imgur.com/b1BaGzk.png)

*install matplotlib*
- Good luck doing this without running into problems.
- The best way is to just get a python distribution with matplotlib included, but if you don't have such a version....
- On linux,this should work:
- ![](http://i.imgur.com/aLsLjF0.png)
- If you try doing that and you get an error about freetype, see [here](http://stackoverflow.com/questions/9829175/pip-install-matplotlib-error-with-virtualenv).

*install Tkinter*
- If you have a python distribution with matplotlib included, or depending on how you installed matplotlib, Tkinter might already be included.
- You can always run the check_dependencies.py script and see if it tells you you need Tkinter.
- On linux, this should work:
- ![](http://i.imgur.com/T8Xpu6Q.png)

*install mpld3*
- Install the latest version.
- ![](http://i.imgur.com/FbcvXkK.png)

*double check*
- Clone the repository.
- ![](http://i.imgur.com/np2dJmt.png)
- Run the check dependencies script.
- ![](http://i.imgur.com/1fQxh4h.png)
- If you don't see that message, you probably missed a step!
- If you did see that message, nice work!

Running the Scripts
-----

######get_commits_per_month.py

Usage: `get_commits_per_month.py <repo_directory> <output_file_path>`

Description: Looks at a cloned repository and outputs a list of months with a count of how many commits there were in each month.

######get_contributors_per_month.py

Usage: `get_contributors_per_month.py <repo_directory> <output_file_path>`

Description: Looks at a cloned repository and outputs a list of months with a count of how many contributors there were in each month.

######get_reddit_posts_per_month.py

Usage: `get_reddit_posts_per_month.py <subreddit> <output_file_path>`

Description: Looks at a subreddit and outputs a list of months with a count of how many new posts there were in each month.

######get_stack_overflow_posts_per_month.py

Usage: `get_stack_overflow_posts_per_month.py <tag> <output_file_path> <api_key(OPTIONAL)>`

Description: Looks at a tag on Stack Overflow and outputs a list of months with a count of how many new questions there were in each month.


Graphing the Output
-------
Each of the four scripts above will output a file in the following format:

![](http://i.imgur.com/zc7Uu9F.png)

Our GraphResults app allows you to pick and choose up to 4 data sets in this format to graph together. This means you can graph the four different sets of data (commits, contributors, reddit posts, stack overflow posts) for the same repository, or you can graph the same set of data for all three repositories (Angular, Bootstrap, Rails).

To run the app, navigate to the graph_results subfolder in our repository and run the run.py script.

![](http://i.imgur.com/eZSz8B8.png)

If you see something like this, then you can navigate to http://127.0.0.1:5000 to use the app. The initial screen lets you pick up to 4 datasets. You must give each a label, with no duplicate labels. The datasets for the three repositories of interest to us (Angular, Rails, Bootstrap) are already in the sample_output folder, so you can choose those, or make your own using the 4 scripts above. It's recommended that you check the "use rolling average" box, as that makes the data smoother and easier to see overall trends.

![](http://i.imgur.com/8Em3gcb.png)

When you click the "submit" button, the the data will be put into a chart for your viewing pleasure.

Results
-----
Note that in the graphs, we scale every dataset to a percentage of the maximum value of that dataset, so each line starts at zero and rises to 100%. This allows us to view the data on the same scale, and we can compare the rates of increase of all of the datasets. 

![Bootstrap](http://i.imgur.com/vhOOFPq.png)
![Angular](http://i.imgur.com/AveyEZA.png)
![Rails](http://i.imgur.com/nWQXc4t.png)


Our question was this: Does the activity on Stack Overflow, or social media sites such as Twitter, drive the number of contributors/size of a project or does actually contributing to the project tend to drive users to use social media? In our hypothesis, we stated that we thought we would see the contributors increase dramatically before social media mentions. This seems to be the case:

![](http://i.imgur.com/bdM7YMg.png)

In each of our three repositories, you can see the contributors per month as well as the commits per month rise quickly before the Stack Overflow or Reddit counts start to increase (as we expected), and you can see the rate of increase of the Stack Overflow/Reddit data always overtakes the rate of increase of the contributors and commits per month. The Stack Overflow questions per month and Reddit posts per month seem to increase at a relatively linear rate, though all seem to be levelling off a bit since early 2014. This could be because people do not feel the need to post a question on Stack Overflow or post on Reddit because similar questions/posts already exist, leading to a reduced rate of new questions/posts.

The Angular graph has a couple of interesting points. In the other two repositories, the commits and contributors lines seem to very closely resemble each other, but for the first few years, Angular has a very small number of contributors per month before it catches up with the commits. Another interesting part of the Angular graph is that development seemed to jump around mid-2012, where everything sharply increases (this is also where the contributors per month line catches up with the commits per month line). By the end of 2013, the commits/contributors are hovering around 100% of their maximum value. If you look at the [number of releases per year](https://github.com/angular/angular.js/releases?), there were 19 in 2013, followed by 56 in 2014, so you can definitely see the effects of this increased development effort. Version 1.0.0 of Angular was released on 14 Jun 2012, around the time that the contributors/commits start to increase sharply, so it's possible that this release led to a large number of new developers. This also may explain why the number of commits/contributors for Angular don't seem to match up early on, as few developers were doing all of the work up to version 1.0.0's release. As more people joined in, each contributor had to do less work on average, so the contributors line catches up with the commits line after this point. 

It seems like we may have an answer to our question, based on the graphs for our 3 interesting respositories. As we guessed in our hypothesis, we see a sharp increase in commits per month and contributors per month before Stack Overflow and Reddit mentions increase. This suggests that in order to gain a "foothold" on social media, there needs to be a certain threshold of contributors. This is similar to how an image or video goes viral on social media - you need a strong foothold before the general public catches on and the image or video starts spreading around the world. If the initial number of people sharing it is too low, it won't go viral. 

- Threats to Validity
not enough data, not enough metrics?

- Future Work
Adjustable timeframes for the scripts, script to run all 4 scripts together, more metrics. 

Demo
-----
[LINK](https://www.youtube.com/watch?v=DWoOsjzO2A4)
