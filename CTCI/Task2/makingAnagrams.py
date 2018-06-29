#!/bin/python3

import math
import os
import random
import re
import sys
import copy


if __name__ == '__main__':
    a = input()
    b = input()
    
    sorted_a = sorted(a)                       ##Storing the string a elements as sorted
    sorted_b = sorted(b)                       ##Storing the string b elements as sorted
    count_ocurrences_a = dict()
    count_occurences_b = dict()
    count = 0
    
    
    for l in sorted_a:                         ##Storing the count of occurences of elements in a
        count_ocurrences_a[l] = a.count(l)  
        
        
    for l in sorted_b:
        count_occurences_b[l] = b.count(l)     ##Storing the count of occurences of elements in b
      
        
    ## Counting the elements by checking common elements ad considering the difference and adding the rest of the elements     
    for key in count_ocurrences_a:             
        if key in b:
            count = count + abs(count_ocurrences_a[key] - count_occurences_b[key])
        else:
            count = count + count_ocurrences_a[key]
            
    for key in count_occurences_b:             
        if key in a:
            continue
        else:
            count = count + count_occurences_b[key]
    print(count)
