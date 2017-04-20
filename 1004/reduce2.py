#!/usr/bin/env python
import sys
import string

result =0
key =None
count =0
currentkey =None
dic ={}
for line in sys.stdin:
    line = line.strip()
    key, value =line.split("\t")
    try:
        val = int(value)
    except ValueError:
        continue

    if key ==currentkey:
        count += 1
        
    else:
        if currentkey:
            dic[currentkey] =count

        currentkey =key
        count =0
        count +=1
if key ==currentkey:
    dic[currentkey] =count
dic = sorted(dic.items(), key =lambda x:x[1], reverse =True)

for tem in dic:
    print("%s\t%s" %(tem[0],tem[1]))


        
