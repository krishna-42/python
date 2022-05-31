#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'FORLoop' function below.
#

def FORLoop():
    # Write your code here
    n = int(input())
    l1 = []
    for i in range(n):
        i = int(input())
        l1.append(i)
    
    print(l1)
    
    iter1 = iter(l1)
    i = 0
    while((i < n)):
        print(next(iter1))
        i  += 1
            
    return(iter1)
    

if __name__ == '__main__':
    try:
        d = FORLoop()
        print(type(d))
        print(next(d))
  
    except StopIteration:
        print('Stop Iteration : No Next Element to fetch')
