#!/usr/bin/env python
import sys
import csv
from datetime import datetime
data =csv.reader(sys.stdin)
next(data)
boroughs =["BRONX","QUEENS","MANHATTAN","STATEN ISLAND","BROOKLYN"]
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
            if entry[13] and entry[13] in boroughs:
                bor =entry[13]
                start1 = entry[1]
                start2 =entry[2]
                end1 =entry[3]
                end2 = entry[4]
                if start1 and start2 and end1 and end2:
                    start =start1 + " " + start2
                    try:
                        start= datetime.strptime(start, date_format)
                        end = end1 +" " + end2
                        end =datetime.strptime(end, date_format)
                        duration =end -start
                        dura = duration.seconds
                        if dura <=600:
                            print("%s, %s\t%s" %(bor,'within10mins',1))
                        elif dura> 600 and dura <1800:
                            print("%s, %s\t%s" %(bor,'within30mins',1))
                        elif dura> 1800 and dura <3600:
                            print("%s, %s\t%s" %(bor,'within1hour',1))
                        elif dura> 3600 and dura <86400:
                            print("%s, %s\t%s" %(bor,'within1day',1))
                        else:
                            print("%s, %s\t%s" %(bor,'over1day',1))
                            
                            
                    except:
                        pass
'''
                        duration_day =duration.days
                        if duration_day <1:
                            if duration.seconds <3600:
                                dura =duration.seconds
                                dura =dura//60
                                dura =str(dura) +"minutes"
                                print("%s %s\t%s" %(bor, dura,1))
                            else:
                                dura = duration.seconds
                                dura = dura //3600
                                dura =str(dura) +'hours'
                                print("%s %s\t%s" %(bor, dura,1))
                        else:
                            dura =duration.days
                            dura = str(dura) +'days'
                            print("%s %s\t%s" %(bor, dura,1))
                    except:
                        pass
'''
            
                



            

