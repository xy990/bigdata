#!/usr/bin/env python
import csv
import sys
from utils import get_type

reader = csv.reader(sys.stdin)
# Skip first row
next(reader, None)
# All possible pre-defined values
valid_list = ['AMTRACK','CONRAIL','DEPT OF CORRECTIONS','DISTRICT ATTORNEY OFFICE','FIRE DEPT (FIRE MARSHAL)',
              'HEALTH & HOSP CORP','LONG ISLAND RAILRD','METRO NORTH','N.Y. HOUSING POLICE','N.Y. POLICE DEPT',
              'N.Y. STATE PARKS','N.Y. STATE POLICE','N.Y. TRANSIT POLICE','NEW YORK CITY SHERIFF OFFICE',
              'NYC DEPT ENVIRONMENTAL PROTECTION','NYC PARKS','NYS DEPT ENVIRONMENTAL CONSERVATION',
              'NYS DEPT TAX AND FINANCE','OTHER','POLICE DEPT NYC','PORT AUTHORITY','SEA GATE POLICE DEPT',
              'STATN IS RAPID TRANS','TRI-BORO BRDG TUNNL','U.S. PARK POLICE']
for entry in reader:

    JURIS_DESC = str(entry[12])
    if JURIS_DESC in valid_list:
        label = 'VALID'
    elif JURIS_DESC == '' or JURIS_DESC is None:
        label = 'NULL'
        JURIS_DESC = 'NULL'
    else:
        label = 'INVALID'
    print('%s\t%s,jurisdiction,%s' % (JURIS_DESC, get_type(JURIS_DESC), label))
    
