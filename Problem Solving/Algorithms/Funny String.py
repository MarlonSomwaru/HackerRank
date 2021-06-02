#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the funnyString function below.
def funnyString(s):
    s=list(s)
    rev_string=s[::-1]
    for i in range(len(s)):
        s[i]=ord(s[i])
        rev_string[i]=ord(rev_string[i])
    diff_1 = [x - s[i - 1] for i, x in enumerate(s)][1:]
    diff_2 = [x - rev_string[i - 1] for i, x in enumerate(rev_string)][1:]
    diff_1=[abs(x) for x in diff_1]
    diff_2=[abs(x) for x in diff_2]

    if(diff_1 == diff_2):
        return 'Funny'
    else: 
        return 'Not Funny'
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = funnyString(s)

        fptr.write(result + '\n')

    fptr.close()
