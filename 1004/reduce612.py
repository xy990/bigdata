#!/usr/bin/env python
import sys
import string
import heapq

count =0
currentkey = None
top5heap = []
for line in sys.stdin:
    line = line.strip()
    key,value =line.split("\t")
    try:
        value =int(value)
    except ValueError:
        continue
    
    if key ==currentkey:
        count += value
        
    else:
        if currentkey:
            if len(top5heap)<5:
                heapq.heappush(top5heap, (count, currentkey))
            elif top5heap[0][0] < count:
                heapq.heappushpop(top5heap, (count, currentkey))

        currentkey =key
        count =0
        count += value
if count>0 and key ==currentkey:
    if len(top5heap)<5:
        heapq.heappush(top5heap, (count, currentkey))
    elif top5heap[0][0] < count:
        heapq.heappushpop(top5heap, (count, currentkey))
        
for v,k in sorted(top5heap,reverse=True):
	print '%s\t%d' %(k,v)
    

    
