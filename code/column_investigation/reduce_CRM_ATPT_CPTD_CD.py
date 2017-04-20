#!/usr/bin/env python
import sys
CRM_ATPT_CPTD_CD_Dict = {}
labels = {}
dtypes = {}
stypes = {}

# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:

    #Remove leading and trailing whitespace
    line = line.strip()
    #if line == '' or line == []:
    #    continue
    #Get key/value 
    CRM_ATPT_CPTD_CD, value = line.split('\t')
    dtype, stype, label = value.split(',')

        
    if CRM_ATPT_CPTD_CD in CRM_ATPT_CPTD_CD_Dict:
        CRM_ATPT_CPTD_CD_Dict[CRM_ATPT_CPTD_CD] = CRM_ATPT_CPTD_CD_Dict[CRM_ATPT_CPTD_CD] + 1
    else:
        CRM_ATPT_CPTD_CD_Dict[CRM_ATPT_CPTD_CD] = 1
    
    if dtype in dtypes:
        dtypes[dtype] = dtypes[dtype] + 1
    else:
        dtypes[dtype] = 1
        
    if stype in stypes:
        stypes[stype] = stypes[stype] + 1
    else:
        stypes[stype] = 1

    if label in labels:
        labels[label] = labels[label] + 1
    else:
        labels[label] = 1        

for key in sorted(CRM_ATPT_CPTD_CD_Dict):
    print ('%s\t%d,%s' %(key, CRM_ATPT_CPTD_CD_Dict[key], 'value'))
    
for key in sorted(dtypes):
    print ('%s\t%d,%s' %(key, dtypes[key], 'dtype'))

for key in sorted(stypes):
    print ('%s\t%d,%s' %(key, stypes[key], 'stype'))

for key in sorted(labels):
    print ('%s\t%d,%s' %(key, labels[key], 'label'))
    
