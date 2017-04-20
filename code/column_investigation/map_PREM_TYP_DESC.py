#!/usr/bin/env python
import csv
import sys
from utils import get_type

reader = csv.reader(sys.stdin)
# Skip first row
next(reader, None)

for entry in reader:
    
    PREM_TYP_DESC = str(entry[16])
    if PREM_TYP_DESC == '' or PREM_TYP_DESC is None or PREM_TYP_DESC == 'N/A':
        label = 'NULL'
        PREM_TYP_DESC = 'NULL'
    else:
        label = 'VALID'
    print('%s\t%s,description,%s' % (PREM_TYP_DESC, get_type(PREM_TYP_DESC), label))
    
