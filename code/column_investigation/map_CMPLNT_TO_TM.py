#!/usr/bin/env python
import csv
import sys
from utils import get_type
import datetime

reader = csv.reader(sys.stdin)
# Skip first row
next(reader, None)

for entry in reader:

    CMPLNT_TO_TM = str(entry[4])

    if CMPLNT_TO_TM == '' or CMPLNT_TO_TM is None:
        label = 'NULL'
        CMPLNT_TO_TM = 'NULL'
    else:
        try:
            # If the transformation fails, then it is invalid
            datetime.datetime.strptime(CMPLNT_TO_TM, '%H:%M:%S')
            label = 'VALID'
        except ValueError:
            label = 'INVALID'


    print('%s\t%s,time,%s' % (CMPLNT_TO_TM, get_type(CMPLNT_TO_TM), label))
    
