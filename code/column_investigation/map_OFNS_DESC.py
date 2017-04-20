#!/usr/bin/env python
import csv
import sys
from utils import get_type

reader = csv.reader(sys.stdin)
# Skip first row
next(reader, None)

for entry in reader:

    OFNS_DESC = str(entry[7])
    if OFNS_DESC == '' or OFNS_DESC is None or OFNS_DESC == 'N/A':
        label = 'NULL'
        OFNS_DESC = 'NULL'
    else:
        label = 'VALID'
    print('%s\t%s,description,%s' % (OFNS_DESC, get_type(OFNS_DESC), label))
    
