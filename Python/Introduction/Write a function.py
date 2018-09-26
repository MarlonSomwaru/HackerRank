# Author: Marlon Somwaru
# Website: MarlonSomwaru.com
# Github: https://github.com/msomwaru13
# HackerRank: https://www.hackerrank.com/MarlonS

def is_leap(year):
    leap = False
    
    if(year%4==0 and (year%400==0 or year%100 !=0)):
        leap=True
    
    return leap