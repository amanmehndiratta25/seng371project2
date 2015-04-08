import sys
import subprocess

def main():
    if len(sys.argv) == 3:
    	repo_directory = str(sys.argv[1])
        output_file = str(sys.argv[2])
    else:
    	print "Usage: get_commits_per_month.py <repo_directory> <output_file_path>"
        sys.exit(2)

    # Run git shortlog --since <date> --until <date> | grep -E '^[ ]+\w+' | wc -l
    # for each month of the year since 2008
    # CAREFUL: If you use dates in the future, it will have unexpected behaviour.
    months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    years = [2008, 2009, 2010, 2011, 2012, 2013, 2014]


    file = open(output_file, 'w')

    for year in years:
        for month in months:
            since = str(year) + "-" + str(month)

            until = str(year) + "-" + str(month + 1)
            if month == 12:
                until = str(year + 1) + "-01"

            gitShortlogProcess = subprocess.Popen(("git", "-C", repo_directory, "shortlog", "--since", since + "-01", "--until", until  + "-01"), stdout=subprocess.PIPE)
            grepProcess = subprocess.Popen(("grep", "-E", "^[ ]+\w+"), stdin=gitShortlogProcess.stdout, stdout=subprocess.PIPE)
            numberOfCommits = subprocess.check_output(("wc", "-l"), stdin=grepProcess.stdout)

            file.write(since + " " + str(int(numberOfCommits)) + '\n')

if __name__ == "__main__":
	main()
