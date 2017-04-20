#!/usr/bin/env python
import sys
import string

result =0
currentkey =None
output =[]
for line in sys.stdin:
    line = line.strip()
    key, value =line.split("\t")
    try:
        val = int(value)
    except ValueError:
        continue

    if key ==currentkey:
        result += val
    else:
        if currentkey:
            print("%s\t%s" %(currentkey, result))
        currentkey =key
        result =0
        result +=val


print("%s\t%s" %(currentkey, result))

#hadoopy.writetb(hdfs_path, [("abc.txt", open("abc.txt").read())])
        
