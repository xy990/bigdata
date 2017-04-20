#!/usr/bin/env python
import csv
import sys
from utils import get_type
import datetime

reader = csv.reader(sys.stdin)
# Skip first row
next(reader, None)

for entry in reader:

    CMPLNT_FR_TM = str(entry[2])

    if CMPLNT_FR_TM == '' or CMPLNT_FR_TM is None:
        label = 'NULL'
        CMPLNT_FR_TM = 'NULL'
    else:
        try:
            # If the transformation fails, then it is invalid
            datetime.datetime.strptime(CMPLNT_FR_TM, '%H:%M:%S')
            label = 'VALID'
        except ValueError:
            label = 'INVALID'


    print('%s\t%s,time,%s' % (CMPLNT_FR_TM, get_type(CMPLNT_FR_TM), label))
    
