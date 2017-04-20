#!/usr/bin/python


import sys
import csv

reader = csv.reader(sys.stdin)
next(reader, None)

for entry in reader:
	PD_DESC = str(entry[9])
	if len(PD_DESC) == 3:
		label = 'NULL'
	else:
		label = PD_DESC
	print label

