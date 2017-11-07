#!/usr/bin/env python
import csv
import sys
#from utils import get_type

reader = csv.reader(sys.stdin)
# Skip first row
next(reader, None)

for entry in reader:
    HADEVELOPT = str(entry[18])
    #DATE = str(entry[1])
    #if DATE[-4:] == '2006':
    if len(HADEVELOPT) == 3:
        label = 'NULL'
    else:
        label = HADEVELOPT
    print label
