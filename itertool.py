#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'usingiter' function below.
#
# The function is expected to return a TUPLE.
# The function accepts following parameters:
#  1. TUPLE tupb
#

def performIterator(tuplevalues):
    # Write your code here
    import itertools
    

    tup1,tup2,tup3,tup4 = tuplevalues
    mainlist = []
    list1 = []
    count = 0
    for i in itertools.cycle(tup1):
        if count>len(tup1)-1:
            break
        else:
            list1.append(i)
            count +=1
    tuple1 = tuple(list1)
    mainlist.append(tuple1[0:4])        
    #mainlist.append(tuple(list1))

    repeattuple = list(itertools.repeat(tup2[0],len(tup2)))
    #print(repeattuple)
    mainlist.append(tuple(repeattuple))

    #prodtuple = list(itertools.accumulate(tup3,operator.mul))
    prodtuple = list(itertools.accumulate(tup3))
    mainlist.append(tuple(prodtuple))

    chaintuple = list(itertools.chain(tup1,tup2,tup3,tup4))
    mainlist.append(tuple(chaintuple))

    falsetuple = (list(itertools.filterfalse(lambda x : x % 2 == 0, chaintuple)))
    mainlist.append(tuple(falsetuple))

    return(tuple(mainlist))

if __name__ == '__main__':

    length = int(input().strip())

    qw1 = []
    for i in range(4):
        qw2 = []
        for _ in range(length):
            qw2_item = int(input().strip())
            qw2.append(qw2_item)
        qw1.append(tuple(qw2))
    tupb = tuple(qw1)

    q = performIterator(tupb)
    print(q)
