#!/usr/bin/env python
import sys
X_COORD_CD_Dict = {}
labels = {}
dtypes = {}
stypes = {}

# input comes TOom STDIN (stream data that goes to the program)
for line in sys.stdin:

    #Remove leading and trailing whitespace
    line = line.strip()
    #if line == '' or line == []:
    #    continue
    #Get key/value 
    X_COORD_CD, value = line.split('\t')
    dtype, stype, label = value.split(',')

        
    if X_COORD_CD in X_COORD_CD_Dict:
        X_COORD_CD_Dict[X_COORD_CD] = X_COORD_CD_Dict[X_COORD_CD] + 1
    else:
        X_COORD_CD_Dict[X_COORD_CD] = 1
    
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

for key in sorted(X_COORD_CD_Dict):
    print ('%s\t%d,%s' %(key, X_COORD_CD_Dict[key], 'value'))
    
for key in sorted(dtypes):
    print ('%s\t%d,%s' %(key, dtypes[key], 'dtype'))

for key in sorted(stypes):
    print ('%s\t%d,%s' %(key, stypes[key], 'stype'))

for key in sorted(labels):
    print ('%s\t%d,%s' %(key, labels[key], 'label'))
    
