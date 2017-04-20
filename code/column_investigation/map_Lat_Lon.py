#!/usr/bin/env python
import csv
import sys
from utils import get_type

reader = csv.reader(sys.stdin)
# Skip first row
next(reader, None)

for entry in reader:

    Lat_Lon = str(entry[23])
    
    if Lat_Lon == '' or Lat_Lon is None:
        label = 'NULL'
        Lat_Lon = 'NULL'
    else:
        # Check whether value pairs are corresponding correctly to original values
        Latitude = str(entry[21])
        Longitude = str(entry[22])
        if Lat_Lon.split(',')[0][1:] == Latitude and Lat_Lon.split(',')[1][1:-1] == Longitude:
            label = 'VALID'
        else:
            label = 'INVALID'
    print('%s\t%s,coordinate,%s' % (Lat_Lon, get_type(Lat_Lon), label))
    
