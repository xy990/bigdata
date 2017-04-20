#!/usr/bin/env python
import csv
import sys
from utils import get_type

reader = csv.reader(sys.stdin)
# Skip first row
next(reader, None)

for entry in reader:

    PD_CD = str(entry[8])
    # Check whether this is a three-digit code
    if len(PD_CD) == 3:
        label = 'VALID'
    elif PD_CD == '' or PD_CD is None:
        label = 'NULL'
        PD_CD = 'NULL'
    else:
        label = 'INVALID'
    print('%s\t%s,code,%s' % (PD_CD, get_type(PD_CD), label))
    
