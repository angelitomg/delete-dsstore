#!/bin/python

#
# delete-dssstore.py
#
# A simple python script to delete .DS_Store files
#
# Angelito M. Goulart
# www.angelitomg.com
#
# April/2013
#

import os
import sys

# Help function
def showhelp():
	print "Usage: delete-dsstore.py PATH"
	print "Example: delete-dsstore.py /Users/angelito"


if len(sys.argv) > 1:

	# Check if parameter is a dir
	if os.path.isdir(sys.argv[1]):

		# Clear file counter
		i = 0;

		# Get path
		path  = sys.argv[1];

		# Runs through all files in the directory
		for root, sub, files in os.walk(path):
			
			for file in files:

				# Checks if exists .DS_Store file
				if file == ".DS_Store":

					# Get full path of current .DS_Store file
					fullpath = os.path.abspath(os.path.join(root, file))
					print "Deleting " + fullpath

					# Remove file
					os.remove(fullpath)
					i += 1

		print str(i) + " files deleted";

	elif sys.argv[1] == '--help':
		
		# Show help message
		showhelp()

	else:

		print "Argument must be a valid directory"

else:

	showhelp()

