#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    if (len(magazine) < len(note)):
        print('No')
        return
    else:
        if (len(magazine) == len(note)):
            if(Counter(note) - Counter(magazine) == {}):
                print('Yes')
            else:
                print('No')
                return
        else:
            for word in note:
                if magazine.count(word) < note.count(word):
                    print ('No')
                    return
    print('Yes')
    
    
if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])
    
    magazine = input().rstrip().split()

    note = input().rstrip().split()
    
    checkMagazine(magazine, note)
    
        
                   
    
