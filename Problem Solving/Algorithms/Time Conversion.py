#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    temp=list(s)
    if s[-2] == 'P' and s[0:2] == '12':
        temp=temp[0:8]
        temp="".join(temp)
        return temp
    elif s[-2] == 'P':
        input_hour=int(s[0:2])
        input_hour+=12
        input_hour=str(input_hour)
        input_hour=list(input_hour)
        temp[0:2]=input_hour
        temp="".join(temp)
        return temp[0:8]

    elif s[-2] == 'A' and s[0:2] == '12':
        temp=temp[0:8]
        temp[0:2]='00'
        temp="".join(temp)
        return temp
    elif s[-2] == 'A':
        temp=temp[0:8]
        temp="".join(temp)
        return temp

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
