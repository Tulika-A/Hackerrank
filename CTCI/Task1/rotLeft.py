# -*- coding: utf-8 -*-
"""
Created on Mon May 28 11:04:16 2018

@author: astha
"""

#!/bin/python3
'''
Cracking the Coding Interview @ hackerrank

Given an array 'a' of 'n' integers and a number,'d',perform  left rotations on the array.
Then print the updated array as a single line of space-separated integers.
'''


import math
import os
import random
import re
import sys

# Complete the rotLeft function below.
def rotLeft(a, d):
    newa = []
    for i in range(d, n):
        newa.append(a[i])
    for i in range(0, d):
        newa.append(a[i])
    return newa    
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    result = rotLeft(a, d)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
