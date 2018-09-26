# Author: Marlon Somwaru
# Website: MarlonSomwaru.com
# Github: https://github.com/msomwaru13
# HackerRank: https://www.hackerrank.com/MarlonS

n = int(input())
s = set(map(int, input().split()))
Number_Ops = int(input())

for i in range(Number_Ops):
    command_input=input().split()
    
    if(len(command_input)==1):
        s.pop()
    elif(command_input[0]=='remove'):
        s.remove(int(command_input[1]))
    elif(command_input[0]=='discard'):
        s.discard(int(command_input[1]))
print(sum(s))