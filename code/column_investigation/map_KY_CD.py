#!/usr/bin/env python
import csv
import sys
from utils import get_type

reader = csv.reader(sys.stdin)
# Skip first row
next(reader, None)

for entry in reader:

    KY_CD = str(entry[6])
    # Check whether this is a three-digit code
    if len(KY_CD) == 3:
        label = 'VALID'
    elif KY_CD == '' or KY_CD is None:
        label = 'NULL'
        KY_CD = 'NULL'
    else:
        label = 'INVALID'
    print('%s\t%s,code,%s' % (KY_CD, get_type(KY_CD), label))
    
