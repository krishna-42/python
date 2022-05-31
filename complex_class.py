 #!/bin/python3

import math
import os
import random
import re
import sys



#
#Write your code here
class comp():
    def __init__(self,rnum,inum):
        self.rnum = rnum
        self.inum = inum
        
        
    def add(self,obj):
        self.obj = obj
        c1 = complex(self.rnum, self.inum)
        c2 = complex(obj.rnum, obj.inum)
        sum = format((c1 + c2),"g").replace('j','i')
        print("Sum of the two Complex numbers:" + sum)
        
    
    def sub(self,obj):
        self.obj = obj
        c1 = complex(self.rnum, self.inum)
        c2 = complex(obj.rnum, obj.inum)
        diff = format((c1 - c2),"g").replace('j','i')
        print("Substraction of the two Complex numbers:" + diff)
        

if __name__ == '__main__':
    
    real1 = int(input().strip())
    img1 = int(input().strip())
    
    real2 = int(input().strip())
    img2 = int(input().strip())
    
    p1 = comp(real1,img1)
    p2 = comp(real2,img2)

    p1.add(p2)
    p1.sub(p2)

