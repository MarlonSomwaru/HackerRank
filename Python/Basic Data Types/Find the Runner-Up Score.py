# Author: Marlon Somwaru
# Website: MarlonSomwaru.com
# Github: https://github.com/msomwaru13
# HackerRank: https://www.hackerrank.com/MarlonS

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    unique_list=[]
    for x in arr:
        if x not in unique_list:
            unique_list.append(x)
    unique_list=sorted(unique_list)
    print(unique_list[-2])