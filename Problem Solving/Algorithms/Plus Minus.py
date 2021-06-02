#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    pos_count=0
    neg_count=0
    zero_count=0
    size_arr=len(arr)
    
    for i in arr:
        if i==0:
            zero_count+=1
        elif i>0:
            pos_count+=1
        elif i<0:
            neg_count+=1
    print(round(pos_count/size_arr,6))
    print(round(neg_count/size_arr,6))
    print(round(zero_count/size_arr,6))

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
