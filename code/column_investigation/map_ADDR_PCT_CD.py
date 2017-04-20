#!/usr/bin/env python
import csv
import sys
from utils import get_type

reader = csv.reader(sys.stdin)
# Skip first row
next(reader, None)
# This list comes from http://www.nyc.gov/html/nypd/html/home/precincts.shtml
valid_list = ['1','5','6','7','9','10','13','14','17','18','19','20','22',
              '23','24','25','26','28','30','32','33','34','40','41','42',
              '43','44','45','46','47','48','49','50','52','60','61','62',
             '63','66','67','68','69','70','71','72','73','75','76','77',
             '78','79','81','83','84','88','90','94','100','101','102',
             '103','104','105','106','107','108','109','110','111',
             '112','113','114','115','120','121','122','123']
for entry in reader:
    
    ADDR_PCT_CD = str(entry[14])
    if ADDR_PCT_CD in valid_list:
        label = 'VALID'
    elif ADDR_PCT_CD == '' or ADDR_PCT_CD is None:
        label = 'NULL'
        ADDR_PCT_CD = 'NULL'
    else:
        label = 'INVALID'
    print('%s\t%s,precinct,%s' % (ADDR_PCT_CD, get_type(ADDR_PCT_CD), label))
    
