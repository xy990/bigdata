#!/usr/bin/env python
import sys
import string
import collections
#from Queue import PriorityQueue
count =0
key =None
currentkey =None

dic ={}

for line in sys.stdin:
    line = line.strip()
    key,value =line.split('\t', 1)

    if key ==currentkey:
        
        count +=1


    else:
        if currentkey:
            #pq.put(count,currentkey)
	    dic[currentkey] =count
	
        currentkey =key
        count =0
        count +=1
        #pq.put(count, currentkey)
            
if key ==currentkey:
    dic[currentkey] =count
dic =sorted(dic.items(),key =lambda x:x[1], reverse =True)
for tem in dic:
    print("%s\t%s" %(tem[0], tem[1]))
