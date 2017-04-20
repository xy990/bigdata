#!/usr/bin/env python
import csv
import sys

reader = csv.reader(sys.stdin)

next(reader, None)
offense = {'FELONY':0,'MISDEMEANOR':0,'VIOLATION':0}

for entry in reader:
    LAW_CAT_CD = str(entry[11])
    DATE = str(entry[1])
    if DATE[:2] == '06':
        if LAW_CAT_CD == 'FELONY':
            offense['FELONY'] += 1
        elif LAW_CAT_CD == 'MISDEMEANOR':
            offense['MISDEMEANOR'] += 1
        elif LAW_CAT_CD == 'VIOLATION':
            offense['VIOLATION'] += 1
        #else:
            #offense['else'] += 1
    #else:
        #offense['invalid'] += 1
for k in offense.keys():
    print '%s\t%d' % (k,offense[k])
