#!/usr/bin/env python
import csv
import sys
from utils import get_type

reader = csv.reader(sys.stdin)
# Skip first row
next(reader, None)

for entry in reader:

    X_COORD_CD = str(entry[19])
    if X_COORD_CD == '' or X_COORD_CD is None:
        label = 'NULL'
        X_COORD_CD = 'NULL'
    else:
        # Based on boxplot, we consider values in the following range as valid ones
        if float(X_COORD_CD) >= 954846 and float(X_COORD_CD) <= 1053121:
            label = 'VALID'
        else:
            label = 'INVALID'
    print('%s\t%s,coordinate,%s' % (X_COORD_CD, get_type(X_COORD_CD), label))
    
