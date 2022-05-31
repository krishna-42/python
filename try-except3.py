#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'Bank_ATM' function below.
#
# Define the Class for user-defined exceptions "MinimumDepositError" and "MinimumBalanceError" here
class MinimumDepositError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return(str(self.value))

class MinimumBalanceError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return(str(self.value))





def Bank_ATM(balance,choice,amount):
    # Write your code here
    if balance < 500:
        raise ValueError("As per the Minimum Balance Policy, Balance must be at least 500")
    else:
        if choice == 1:
            try:
                if amount < 2000:
                    raise MinimumDepositError("The Minimum amount of Deposit should be 2000.")
                else:
                    balance = balance + amount
                    print("Updated Balance Amount:  " + str(balance))
            except MinimumDepositError as md:
                print(md)
        elif choice == 2:
            try:
                balance = balance - amount
                if (balance < 500):
                    raise MinimumBalanceError("You cannot withdraw this amount due to Minimum Balance Policy")
                else:
                   print("Updated Balance Amount:  " + str(balance))
            except MinimumBalanceError as mb:
                print(mb)
        #else:
        #    print("Invalid choice")
               
        

if __name__ == '__main__':
    
    bal = int(input())
    ch = int(input())
    amt = int(input())
    
    try:
        Bank_ATM(bal,ch,amt)
    
    
    except ValueError as e:
        print(e)
    except MinimumDepositError as e:
        print(e)
    except MinimumBalanceError as e:
        print(e)