#!/usr/bin/env python
import csv
import sys
from utils import get_type

reader = csv.reader(sys.stdin)
# Skip first row
next(reader, None)
# All possible pre-defined values
valid_list = ['ATTEMPTED','COMPLETED']
for entry in reader:

    CRM_ATPT_CPTD_CD = str(entry[10])
    if CRM_ATPT_CPTD_CD in valid_list:
        label = 'VALID'
    elif CRM_ATPT_CPTD_CD == '' or CRM_ATPT_CPTD_CD is None:
        label = 'NULL'
        CRM_ATPT_CPTD_CD = 'NULL'
    else:
        label = 'INVALID'
    print('%s\t%s,flag,%s' % (CRM_ATPT_CPTD_CD, get_type(CRM_ATPT_CPTD_CD), label))
    
