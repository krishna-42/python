#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'strmethod' function below.
#
# The function accepts following parameters:
#  1. STRING para
#  2. STRING spch1
#  3. STRING spch2
#  4. LIST li1
#  5. STRING strf
#

def stringmethod(para, special1, special2, list1, strfind):
    # Write your code here
        # Sol 1

        word1 = para.translate({ ord(c): None for c in special1 })
        
        print(word1)
        # Sol 2
        new_string = word1[:70]    
        rword2 = new_string[::-1]
        print(rword2) #output 1
    
        # Sol 3
        new_word = rword2.replace(" ","")
        #for chars in special2:
        new_str = special2.join(new_word) #.replace(" ",chars)
        
        print(new_str) #output 2
        
        # Sol 4
        flag = 0
        for string in list1:
            if string in para:
                flag = 1
            else: flag = 0
            
        if (flag == 1):
            print("Every string in", list1, "were present") #output 3
        else: print("Every string in", list1, "were not present")
        
        #sol 5
        split_word1 = word1.split() #re.findall(r'\w+', word1)
        print(list(split_word1[:20])) # output 4
    
        #sol 6
        
        wword = []
        for word in word1.split():
            wcount = word1.split().count(word)
            
            if (( wcount < 3) and (word not in wword)):
                wword.append(word)
           
         
        print(wword[-20:]) #output 5
    
        #sol 7
        print(word1.rindex(strfind)) #output6
        
    
    

if __name__ == '__main__':
    para = input()

    spch1 = input()

    spch2 = input()
    
    qw1_count = int(input().strip())

    qw1 = []

    for _ in range(qw1_count):
        qw1_item = input()
        qw1.append(qw1_item)

    strf = input()

    stringmethod(para, spch1, spch2, qw1, strf)
