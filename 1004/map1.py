#!/usr/bin/env python
import sys
import csv
from datetime import datetime
data =csv.reader(sys.stdin)
next(data)
for entry in data:
    dt = entry[1]
    if dt:
        dt = datetime.strptime(dt, '%m/%d/%Y')
        lower_bound = datetime.strptime('01/01/2006', '%m/%d/%Y')
        upper_bound = datetime.strptime('12/31/2015', '%m/%d/%Y')
        if dt >upper_bound or dt < lower_bound:
            pass
        else:
            bor = entry[13]
            count =1
            if bor:
                print("%s\t%s" %(bor, count))



    
