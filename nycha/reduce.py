#!/usr/bin/env python
import sys
D = {}

for line in sys.stdin:

    HADEVELOPT = line.strip()
         
    if HADEVELOPT in D:
        D[HADEVELOPT] += 1
    else:
        D[HADEVELOPT] = 1

for k in sorted(D):
    print '%s\t%d' %(k, D[k])
