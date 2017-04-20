#!/usr/bin/env python
import sys
import csv
from datetime import datetime
data =csv.reader(sys.stdin)
next(data)

date_format = "%m/%d/%Y %H:%M:%S"
for entry in data:
    dt = entry[1]
    if dt:
        dt = datetime.strptime(dt, '%m/%d/%Y')
        lower_bound = datetime.strptime('01/01/2006', '%m/%d/%Y')
        upper_bound = datetime.strptime('12/31/2015', '%m/%d/%Y')
        if dt >upper_bound or dt < lower_bound:
            pass
        else:
    
            start1 = entry[1]
            start2 =entry[2]
            end1 =entry[3]
            end2 = entry[4]
            if start1 and start2 and end1 and end2:
                start =start1 + " " + start2
                start= datetime.strptime(start, date_format)
                end = end1 +" " + end2
                end =datetime.strptime(end, date_format)
                duration =end -start
                duration_day =duration.days
                if duration_day <1:
                    if duration.seconds <3600:
                        dura =duration.seconds
                        dura =dura//60
                        dura =str(dura) +"minutes"
                        print("%s\t%s" %(dura,1))
                    else:
                        dura = duration.seconds
                        dura = dura //3600
                        dura =str(dura) +'hours'
                        print("%s\t%s" %(dura,1))
                else:
                    dura =duration.days
                    dura = str(dura) +'days'
                    print("%s\t%s" %(dura,1))



            

