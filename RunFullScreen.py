#!/usr/bin/env python2
import GoL
from time import sleep
import os
rows, columns = os.popen('stty size', 'r').read().split()
rows = int(rows)/2 -1
columns = int(columns)/2
brd = ""
while True:
	brd = GoL.Board(columns,rows)
	brd.IconNoLife = " "
	# for x in xrange(500):
	while True:
		brd.advance()
		if str(brd).find("#") < 0:
			break
		# print '\n'
		brd.printAsString()
		sleep(0.1)