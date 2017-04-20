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
       
            if entry[16]:
     		prem_type =entry[16]
                print("%s\t%s" %(prem_type, 1))



    
