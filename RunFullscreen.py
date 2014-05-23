#!/usr/bin/env python2
from time import sleep
import os
import GoL
rows, columns = os.popen('stty size', 'r').read().split()
rows = int(rows)-1
columns = int(columns)
brd = ""
while True:
	brd = GoL.Board(rows,columns)
	brd.IconNoLife = " "
	for x in xrange(500):
		brd.advance()
		if str(brd).find("#") < 0:
			break
		# print '\n'
		brd.printAsString()
		sleep(0.1)