#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    arr=sorted(arr)
    min_sum=0
    max_sum=0
    temp1=arr[0:4]
    temp2=arr[1:5]
    for i in temp1:
        min_sum+=i
    for i in temp2:
        max_sum+=i
    print(min_sum, max_sum)

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
