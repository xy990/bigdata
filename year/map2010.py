#!/usr/bin/env python
import csv
import sys

reader = csv.reader(sys.stdin)
next(reader, None)

for entry in reader:
    PD_DESC = str(entry[9])
    DATE = str(entry[1])
    if DATE[-4:] == '2010':
    	if len(PD_DESC) == 3:
        	label = 'NULL'
    	else:
        	label = PD_DESC
	print label
