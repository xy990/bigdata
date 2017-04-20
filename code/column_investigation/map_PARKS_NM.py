#!/usr/bin/env python
import csv
import sys
from utils import get_type

reader = csv.reader(sys.stdin)
# Skip first row
next(reader, None)

for entry in reader:

    PARKS_NM = str(entry[17])
    if PARKS_NM == '' or PARKS_NM is None or PARKS_NM == 'N/A':
        label = 'NULL'
        PARKS_NM = 'NULL'
    else:
        label = 'VALID'
    print('%s\t%s,name,%s' % (PARKS_NM, get_type(PARKS_NM), label))
    
