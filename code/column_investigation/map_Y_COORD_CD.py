#!/usr/bin/env python
import csv
import sys
from utils import get_type

reader = csv.reader(sys.stdin)
# Skip first row
next(reader, None)

for entry in reader:

    Y_COORD_CD = str(entry[20])
    if Y_COORD_CD == '' or Y_COORD_CD is None:
        label = 'NULL'
        Y_COORD_CD = 'NULL'
    else:
        label = 'VALID'
    print('%s\t%s,coordinate,%s' % (Y_COORD_CD, get_type(Y_COORD_CD), label))
    
