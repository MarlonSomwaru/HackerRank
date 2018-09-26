# Author: Marlon Somwaru
# Website: MarlonSomwaru.com
# Github: https://github.com/msomwaru13
# HackerRank: https://www.hackerrank.com/MarlonS

if __name__ == '__main__':
    N = int(input())
    
    arr=[]
    for i in range(0,N):
        Action=input().split()
        if Action[0]=="insert":
            arr.insert(int(Action[1]),int(Action[2]))
        elif Action[0]=="print":
            print(arr)
        elif Action[0]=="remove":
            arr.remove(int(Action[1]))
        elif Action[0]=="append":
            arr.append(int(Action[1]))
        elif Action[0]=="sort":
            arr.sort()
        elif Action[0]=="pop":
            arr.pop()
        elif Action[0]=="reverse":
            arr.reverse()