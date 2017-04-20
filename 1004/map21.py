#!/usr/bin/env python
import sys
import csv
from datetime import datetime
data =csv.reader(sys.stdin)
next(data)

classes = ['PETIT LARCENY',
 'HARRASSMENT 2',
 'ASSAULT 3 & RELATED OFFENSES',
 'CRIMINAL MISCHIEF & RELATED OF',
 'GRAND LARCENY',
 'DANGEROUS DRUGS',
 'OFF. AGNST PUB ORD SENSBLTY &',
 'ROBBERY',
 'BURGLARY',
 'FELONY ASSAULT']
for entry in data:
    dt = entry[1]
    if dt:
        try:
            dt = datetime.strptime(dt, '%m/%d/%Y')
        except:
            pass
        lower_bound = datetime.strptime('01/01/2006', '%m/%d/%Y')
        upper_bound = datetime.strptime('12/31/2015', '%m/%d/%Y')
        if dt >upper_bound or dt < lower_bound:
            pass
        else:
            if entry[7] and entry[7] in classes:
                crime_class = entry[7]#OFNS_DESC
                juri = entry[12]
                count =1
                print("%s, %s\t%s" %(crime_class, juri, count))

