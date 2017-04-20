#!/usr/bin/env python
import csv
import sys
from utils import get_type

reader = csv.reader(sys.stdin)
# Skip first row
next(reader, None)

# All possible pre-defined values
valid_list = ['INSIDE','OPPOSITE OF','OUTSIDE', 'REAR OF', 'FRONT OF']
for entry in reader:

    LOC_OF_OCCUR_DESC = str(entry[15])
    if LOC_OF_OCCUR_DESC in valid_list:
        label = 'VALID'
    elif LOC_OF_OCCUR_DESC == '' or LOC_OF_OCCUR_DESC == ' ' or LOC_OF_OCCUR_DESC is None:
        label = 'NULL'
        LOC_OF_OCCUR_DESC = 'NULL'
    else:
        label = 'INVALID'
    print('%s\t%s,description,%s' % (LOC_OF_OCCUR_DESC, get_type(LOC_OF_OCCUR_DESC), label))
    
