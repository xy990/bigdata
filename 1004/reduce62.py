#!/usr/bin/env python
import sys
import string

result =0
key =None
currentkey =None
output =[]
for line in sys.stdin:
    line = line.strip()
    key, value =line.split("\t",1)
    try:
        val = int(value)
    except ValueError:
        continue

    if key ==currentkey:
        result += val
    else:
        if currentkey:
            print("%s, %s, %s" %(currentkey, result, 1))

        currentkey =key
        result =0
        result +=val

if currentkey:
    print("%s, %s, %s" %(currentkey, result, 1))


        
