#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'Magic_const' function below.
#
# 
#
# The function accepts INTEGER n1 as parameter.
#

def generator_Magic(n1):
    # Write your code here
     n = 3
    while (n <= n1):
        yield ((n * (n**2 + 1)) / 2)
        n += 1

if __name__ == '__main__':

    n = int(input().strip())
    
    for i in generator_Magic(n):
        print(int(i))

    gen1 = generator_Magic(n)
    print(type(gen1))
