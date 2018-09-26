# Author: Marlon Somwaru
# Website: MarlonSomwaru.com
# Github: https://github.com/msomwaru13
# HackerRank: https://www.hackerrank.com/MarlonS

#!/bin/python3

N = int(input())
if N%2!=0:
    print("Weird")
elif (N%2==0 and (N>=2 and N<=5)):
    print("Not Weird")
elif (N%2==0 and(N>=6 and N<=20)):
    print("Weird")
elif (N%2==0 and N>20):
    print("Not Weird")
