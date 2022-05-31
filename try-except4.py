#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'Library' function below.
#

 
def Library(memberfee,installment,book):
    # Write your code here
    booklist = ['philosophers stone','chamber of secrets','prisoner of azkaban','goblet of fire','order of phoenix','half blood prince','deathly hallows 1','deathly hallows 2']
    
    if (installment > 3):
        raise ValueError("Maximum Permitted Number of Installments is 3")
    elif (installment == 0):
        raise ZeroDivisionError("Number of Installments cannot be Zero.")
    else:
        amount_per_inst = memberfee / installment
        print("Amount per Installment is  " + str(amount_per_inst))
        
        if (str(book).lower() not in booklist):
            raise NameError("No such book exists in this section")
        else:
            print("It is available in this section")

if __name__ == '__main__':
    
    memberfee = int(input())
    installment = int(input())
    book = input()
    
    try:
        Library(memberfee,installment,book)
        
    except ZeroDivisionError as e:
        print(e)
    except ValueError as e:
        print(e)
    except NameError as e:
        print(e)