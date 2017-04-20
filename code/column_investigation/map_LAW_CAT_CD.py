#!/usr/bin/env python
import csv
import sys
from utils import get_type

reader = csv.reader(sys.stdin)
# Skip first row
next(reader, None)
valid_list = ['FELONY','MISDEMEANOR','VIOLATION']
for entry in reader:
# All possible pre-defined values
    LAW_CAT_CD = str(entry[11])
    if LAW_CAT_CD in valid_list:
        label = 'VALID'
    elif LAW_CAT_CD == '' or LAW_CAT_CD is None:
        label = 'NULL'
        LAW_CAT_CD = 'NULL'
    else:
        label = 'INVALID'
    print('%s\t%s,code,%s' % (LAW_CAT_CD, get_type(LAW_CAT_CD), label))
    
