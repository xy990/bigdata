#!/usr/bin/env python
import csv
import sys
from utils import get_type

reader = csv.reader(sys.stdin)
# Skip first row
next(reader, None)

for entry in reader:

    Latitude = str(entry[21])
    if Latitude == '' or Latitude is None:
        label = 'NULL'
        Latitude = 'NULL'
    else:
        # There is no outliers showing in boxplot so we make every non-missing values valid
        label = 'VALID'
    print('%s\t%s,latitude,%s' % (Latitude, get_type(Latitude), label))
    
