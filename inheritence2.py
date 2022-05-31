#!/bin/python3

import math
import os
import random
import re
import sys



# Write your code here
class rectangle:
    def display(self):
        print("This is a Rectangle")
        
    def area(self, length, breadth):
        self.length = length
        self.breadth = breadth
        out= "Area of Rectangle is  "+ str(self.length * self.breadth)
        print(out)
        
class square:
    def display(self):
        print("This is a Square")
        
    def area(self, side):
        self.side = side
        square = "Area of square is  "+ str(self.side**2)
        print(square)
    
        
    
    

if __name__ == '__main__':
    
    l = int(input())
    b = int(input())
    s = int(input())

    obj1 = rectangle()
    obj1.display()
    obj1.area(l,b)

    obj2 = square()
    obj2.display()
    obj2.area(s)

