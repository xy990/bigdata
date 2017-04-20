#!/usr/bin/env python
import csv
import sys
from utils import get_type

reader = csv.reader(sys.stdin)
# Skip first row
next(reader, None)
valid_list = ['BRONX','BROOKLYN','MANHATTAN','QUEENS','STATEN ISLAND']
for entry in reader:

    BORO_NM = str(entry[13])
    if BORO_NM in valid_list:
        label = 'VALID'
    elif BORO_NM == '' or BORO_NM is None:
        label = 'NULL'
        BORO_NM = 'NULL'
    else:
        label = 'INVALID'
    print('%s\t%s,borough,%s' % (BORO_NM, get_type(BORO_NM), label))
    
