#!/bin/python3

import math
import os
from posixpath import split
import random
import re
import sys
import datetime


#from datetime import datetime
#
# Complete the 'dateandtime' function below.
#
# The function accepts INTEGER val as parameter.
# The return type must be LIST.
#

def dateandtime(val,tup):
    # Write your code here
    list1 =[]
    if (val == 1):
        yr,mn,dt = tup
        a = datetime.date(yr,mn,dt)
        fdate = str('{:02d}'.format(dt)) + "/" + str('{:02d}'.format(mn)) + "/" + str(yr)
        list1.append(a)
        list1.append(fdate)
    elif (val ==2):
        ts = tup[0]
        dt = datetime.date.fromtimestamp(ts)

        #mn = int(datetime.date(datetime.fromtimestamp(tm)).month)
        #yr = int(datetime.date(datetime.fromtimestamp(tm)).year)
        #ndate = datetime.date(yr,mn,dt)
        list1.append(dt)
        fday = int(dt.strftime('%d'))
        fmn = int(dt.strftime('%m'))
        fyr = int(dt.strftime('%Y'))
        fdate = str('{:02d}'.format(fday)) + "/" + str('{:02d}'.format(fmn)) + "/" + str(fyr)
        list1.append(fdate)
    elif (val ==3):
        hr,mins,sec = tup
        atime = datetime.time(hr,mins,sec)
        hr12 = atime.strftime("%I")
        list1.append(atime)
        list1.append(hr12)
    elif (val ==4):
        yr,mn,dt = tup
        date_obj = datetime.date(yr,mn,dt)
        wday = date_obj.strftime("%A")
        mont = date_obj.strftime("%B")
        dy = date_obj.strftime("%j")
        list1.append(str(wday))
        list1.append(str(mont))
        list1.append(str(dy))
    elif (val ==5):
        yr,mnth,dt,hr,mn,sec = tup
        list1.append(datetime.datetime(yr,mnth,dt,hr,mn,sec))
    else:
        list1=[]
    
    return(list1)
        
       

if __name__ == '__main__':
    val = int(input().strip())
    
    if val ==1 or val==4 or val ==3:
        qw1_count=3
    if val==2:
        qw1_count=1
    if val ==5:
        qw1_count=6
    qw1 = []

    for _ in range(qw1_count):
        qw1_item = int(input().strip())
        qw1.append(qw1_item)
        
    tup=tuple(qw1)
    
    ans = dateandtime(val,tup)
    
    print(ans)