#!/usr/bin/env python
import csv
import sys
from utils import get_type

reader = csv.reader(sys.stdin)
# Skip first row
next(reader, None)

for entry in reader:

    HADEVELOPT = str(entry[18])
    if HADEVELOPT == '' or HADEVELOPT is None or HADEVELOPT == 'N/A':
        label = 'NULL'
        HADEVELOPT = 'NULL'
    else:
        label = 'VALID'
    print('%s\t%s,address,%s' % (HADEVELOPT, get_type(HADEVELOPT), label))
    
