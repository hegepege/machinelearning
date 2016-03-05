#!/usr/bin/python

import glob, os, shutil, sys

ex_no = sys.argv[1]

def move(source_dir, dest_dir):
	files = glob.iglob(os.path.join(source_dir, "*.m"))
	for file in files:
		if os.path.isfile(file):
			print "copying file: " + file
			shutil.copy2(file, dest_dir)


source_dir = "patchlib"
dest_dir = "machine-learning-ex{0}{1}ex{0}{1}lib".format(ex_no, os.sep)
move(source_dir, dest_dir)


source_dir = os.path.join(source_dir, "jsonlab")
dest_dir = os.path.join(dest_dir, "jsonlab")
move(source_dir, dest_dir)
