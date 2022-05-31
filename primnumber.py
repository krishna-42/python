#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'primegenerator' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER num
#  2. INTEGER val
#

def primegenerator(num, val):
    # Write your code here
    out = []
    for n in range(2,num):
        flag = 0
        if (n > 2):
            for i in range(2, n):
                if (n % i) == 0:
                    flag =0
                    break
                else:
                   flag = 1
        else:
            flag = 1
        if ( flag == 1):
            out.append(n)
            
    print(str(out))
    if  (val == 0):
        yield  (" ".join(map(str,out[0::2])))
    elif (val == 1):
        yield  (" ".join(map(str,out[1::2])))
        
        
        

if __name__ == '__main__':

    num = int(input().strip())

    val = int(input().strip())

    for i in primegenerator(num, val):
        print(i,end=" ")
