# seng371project2

Colin Knowles (@knowlesc) and Ryan McDonald (@ryanmcdonald)

Question
-------
Does the activity on Stack Overflow, or social media sites such as Twitter, drive the number of contributors/size of a project or do social media mentions drive the contributors/size?

**Hypotheses**: We think that the number of contributors/project size should drive the mentions on social media. We think that in order to gain a "foothold" on social media-type sites, a project would need a certain number of contributors, so we will see the contributors increase dramatically before we see social media mentions start to increase.

Datasets
-------
**Codebases**: [Angular](https://github.com/angular/angular.js), [Bootstrap](https://github.com/twbs/bootstrap), and [Rails](https://github.com/rails/rails)

**APIs**: [Stack Exchange API](https://api.stackexchange.com), [Reddit API](http://www.reddit.com/dev/api)

**Metrics**: & justification (todo)

Methodology
--------
1) Figure out how to use the APIs of some social media sites
2) Search for mentions of certain projects by date using these APIs
2) Run git log on the codebases to get the number of contributors
3) Compare project statistics with social media information

**TODO: Go into more detail on methodology**

Milestones (Revised March 24, 2015)
-----------------------------------
|#|Milestone|Date|Assignee|Status|
|----|---------|----|------------|------|
|1|**Research Stack Exchange API**|Mar. 13|Ryan|Completed|
|2|**Create Python program to automatically retrieve a count of mentions of a certain project from Stack Exchange API**|Mar. 17|Colin|Completed|
|3|**Create Python program to automatically run git log and get the data we need from a repository (# of contributors, project size)**|Mar. 17|Ryan|Completed|
|4|**Create Python program to automatically retrieve a count of mentions of a certain project from Reddit API**|Mar. 24|Colin|In progress|
|5|**Create Python program to run the previous three programs and graph their outputted data**|Mar. 30|Everyone|In progress|
|6|**Perform analysis on graphs**|Apr. 1|Everyone|In progress|

Tools
-----
our python scripts - todo
(need instructions too)

Results
-----
analysis, answer to question, threats to validity, future work

Demo
-----
a link to a video screencast demonstrating your work!
