#!/usr/bin/env python
import sys
D = {}

for line in sys.stdin:

    PD_DESC = line.strip()
         
    if PD_DESC in D:
        D[PD_DESC] += 1
    else:
        D[PD_DESC] = 1

for k in sorted(D):
    print '%s\t%d' %(k, D[k])
