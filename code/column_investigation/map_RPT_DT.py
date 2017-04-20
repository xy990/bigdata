#!/usr/bin/env python
import csv
import sys
from utils import get_type
import datetime

reader = csv.reader(sys.stdin)
# Skip first row
next(reader, None)

for entry in reader:

    RPT_DT = str(entry[5])

    if RPT_DT == '' or RPT_DT is None:
        label = 'NULL'
        RPT_DT = 'NULL'
    else:
        try:
            # define upper bound and lower bound to exclude outliers
            dt = datetime.datetime.strptime(RPT_DT, '%m/%d/%Y')
            lb = datetime.datetime.strptime('01/01/2006', '%m/%d/%Y')
            ub = datetime.datetime.strptime('12/31/2015', '%m/%d/%Y')
            if dt > ub or dt < lb:
                label = 'INVALID'
            else:
                label = 'VALID'
        except ValueError:
            label = 'INVALID'


    print('%s\t%s,date,%s' % (RPT_DT, get_type(RPT_DT), label))
    
