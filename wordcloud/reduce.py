#!/usr/bin/python


import sys

for line in sys.stdin:
	word = line.split(',')[0]

	print word
