'''
Problem Description: A kidnapper wrote a ransom note but is worried it will be traced back to him through his handwriting. He found a magazine and wants to know if he can cut out whole words
from it and use them to create an untraceable replica of his ransom note. The words in his note are case-sensitive and he must use only whole words available in the magazine.
He cannot use substrings or concatenation to create the words he needs.Given the words in the magazine and the words in the ransom note, print Yes if he can replicate his 
ransom note exactly using whole words from the magazine; otherwise, print No.For example, the note is "Attack at dawn". The magazine contains only "attack at dawn".
The magazine has all the right words, but there's a case mismatch. The answer is No.
''' 
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
    
        
                   
    
