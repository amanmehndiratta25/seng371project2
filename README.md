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
