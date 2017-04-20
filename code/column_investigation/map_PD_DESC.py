#!/usr/bin/env python
import csv
import sys
from utils import get_type

reader = csv.reader(sys.stdin)
# Skip first row
next(reader, None)

for entry in reader:

    PD_DESC = str(entry[9])
    if PD_DESC == '' or PD_DESC is None or PD_DESC == 'N/A':
        label = 'NULL'
        PD_DESC = 'NULL'
    else:
        label = 'VALID'
    print('%s\t%s,description,%s' % (PD_DESC, get_type(PD_DESC), label))
    
