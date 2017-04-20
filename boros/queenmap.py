#!/usr/bin/env python
import csv
import sys

reader = csv.reader(sys.stdin)
# Skip first row
next(reader, None)
brooklyn = {'2006':0,'2007':0,'2008':0,'2009':0,'2010':0,'2011':0,'2012':0,'2013':0,'2014':0,'2015':0,'else':0,'invalid':0}

for entry in reader:
    BORO_NM = str(entry[13])
    year = str(entry[1])
    if BORO_NM == 'QUEENS':
        if year[-4:] == '2006':
            brooklyn['2006'] += 1
        elif year[-4:] == '2007':
            brooklyn['2007'] += 1
        elif year[-4:] == '2008':
            brooklyn['2008'] += 1
        elif year[-4:] == '2009':
            brooklyn['2009'] += 1
        elif year[-4:] == '2010':
            brooklyn['2010'] += 1
        elif year[-4:] =='2011':
            brooklyn['2011'] += 1
        elif year[-4:] == '2012':
            brooklyn['2012'] += 1
        elif year[-4:] == '2013':
            brooklyn['2013'] += 1
        elif year[-4:] == '2014':
            brooklyn['2014'] += 1
        elif year[-4:] == '2015':
            brooklyn['2015'] += 1
        else:
            brooklyn['else'] += 1
    else:
        brooklyn['invalid'] += 1
for k in brooklyn.keys():
    print '%s\t%d' % (k,brooklyn[k])
