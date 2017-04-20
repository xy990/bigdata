#!/usr/bin/env python
import csv
import sys
from utils import get_type

reader = csv.reader(sys.stdin)
# Skip first row
next(reader, None)

for entry in reader:

    Longitude = str(entry[22])
    if Longitude == '' or Longitude is None:
        label = 'NULL'
        Longitude = 'NULL'
    else:
        # Based on boxplot, we consider values in the following range as valid ones
        if -float(Longitude) >= 73.751233647000006 and -float(Longitude) <= 74.106266945000002:
            label = 'VALID'
        else:
            label = 'INVALID'
    print('%s\t%s,longitude,%s' % (Longitude, get_type(Longitude), label))
    
