
from __future__ import print_function

import sys
from pyspark import SparkContext
from csv import reader

if __name__ == "__main__":
    
    sc = SparkContext()
    lines = sc.textFile(sys.argv[1], 1)
    lines = lines.mapPartitions(lambda x: reader(x))

    parking_vio = lines.map(lambda item: (item[11],1)).reduceByKey(lambda x,y: x+y)
    parking_vio.map(lambda item: '%s\t%d' %(item[0],item[1])).saveAsTextFile("task.out")
    sc.stop()
