#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'Handle_Exc1' function below.
#
#

def Handle_Exc1():
    # Write your code here
    a = int(input())
    b = int(input())
    try:
        if ( a > 150 or b < 100):
            raise ValueError("Input integers value out of range.")
        elif ( (a + b) > 400 ):
            print("Their sum is out of range")
        else:
            print("All in range")
    except ValueError as v:
        print(v)
            

if __name__ == '__main__':
    try:
        Handle_Exc1()
    except ValueError as exp:
        print(exp)

