# seng371project2

Colin Knowles (@knowlesc) and Ryan McDonald (@ryanmcdonald)

**Question**: Does the activity on Stack Overflow, or social media sites such as Twitter, drive the number of contributors/size of a project or do social media mentions drive the contributors/size?

**Datasets**: We're thinking of looking at [Angular](https://github.com/angular/angular.js), [Bootstrap](https://github.com/twbs/bootstrap), and [Rails](https://github.com/rails/rails), but we might modify the codebases later on. We plan to use [gitstats](http://gitstats.sourceforge.net), and the [Stack Exchange API](https://api.stackexchange.com) (at least) to gather data on these repositories.

**Hypotheses**: We think that the number of contributors/project size should drive the mentions on social media. 

**Plan of Attack**: 
1) Figure out how to use the APIs of some social media sites
2) Search for mentions of certain projects by date
2) Run gitstats on the codebases
3) Compare project statistics with social media information

**Milestones**:

1) Research Stack Exchange API

Date: March 13

Colin & Ryan

2) Create Python program to automatically retrieve a count of mentions of a certain project from Stack Exchange API

  - to start we are going to look at one month out of every year
  - if the program can do that very easily we want to increase the number of data points

Date: March 17 

Colin & Ryan

3) Create Python program to automatically run gitstats and get the data we need from a repository (# of contributors, project size)

  - same as previous, start out taking a snapshot of one month a year, then expand if possible

Date: March 24

Ryan

4) Create Python program to run the previous two programs and graph their outputted data

  - we are thinking of using matplotlib for this

Date: March 24

Colin

5) Perform analysis on graphs

Date: March 30

