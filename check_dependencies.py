import sys

try:
    import requests
except ImportError:
    print "module requests[security] needs to be installed"
    sys.exit(0)

requests_version = requests.__version__.split('.')
if int(requests_version[0]) < 3 and int(requests_version[1]) < 6:
	print "requests needs to be updated"
        sys.exit(0)

try:
    import praw
except ImportError:
    print "module praw needs to be installed"
    sys.exit(0)

try:
    import flask
except ImportError:
    print "module flask needs to be installed"
    sys.exit(0)

try:
    import matplotlib
except ImportError:
    print "module matplotlib needs to be installed"
    sys.exit(0)

try:
    import Tkinter
except ImportError:
    print "module _tkinter needs to be installed"
    print "sudo apt-get install python-tk"

try:
    import mpld3
except ImportError:
    print "module mpld3 needs to be installed"
    sys.exit(0)


