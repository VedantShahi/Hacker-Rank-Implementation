import math
import os
import random
import re
import sys

#
# Complete the 'countApplesAndOranges' function below.
#
# The function accepts following parameters:
#  1. INTEGER s
#  2. INTEGER t
#  3. INTEGER a
#  4. INTEGER b
#  5. INTEGER_ARRAY apples
#  6. INTEGER_ARRAY oranges
#

def countApplesAndOranges(s, t, a, b, apples, oranges):
    ap=0
    o=0
    for i in range(0,len(apples)):
        if(a+apples[i] in range(s,t+1)):
            ap+=1
    for j in range(0,len(oranges)):
        if(b+ oranges[j] in range(s,t+1)):
            o+=1
    if(ap==0 and o!=0):
        print(o)
    elif(ap!=0 and o==0):
        print(ap)
    
    else:
        print(ap)
        print(o)
        
        
        
    
    
    # Write your code here

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    s = int(first_multiple_input[0])

    t = int(first_multiple_input[1])
