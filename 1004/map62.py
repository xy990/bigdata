#!/usr/bin/env python
import sys
import csv
from datetime import datetime
data =csv.reader(sys.stdin)
next(data)

top5= ['STREET',
 'RESIDENCE - APT. HOUSE',
 'RESIDENCE-HOUSE',
 'RESIDENCE - PUBLIC HOUSING',
 'OTHER']

for entry in data:
    dt = entry[1]
    if dt:
        dt = datetime.strptime(dt, '%m/%d/%Y')
        lower_bound = datetime.strptime('01/01/2006', '%m/%d/%Y')
        upper_bound = datetime.strptime('12/31/2015', '%m/%d/%Y')
        if dt >upper_bound or dt < lower_bound:
            pass
        else:
            
            if entry[16] and entry[16] in top5:
		prem_type =entry[16]
                
                if entry[7]:
		    offense =entry[7]
                    print("%s, %s\t%s"%(prem_type, offense, 1))



    
