# Author: Marlon Somwaru
# Website: MarlonSomwaru.com
# Github: https://github.com/msomwaru13
# HackerRank: https://www.hackerrank.com/MarlonS

def Set_Update(set_name):
    temp_set = set(map(int, input().split()))
    set_name.update(temp_set)
    return set_name
 
def Set_SymDiff_Update(set_name):
    temp_set = set(map(int, input().split()))
    set_name.symmetric_difference_update(temp_set)
    return set_name

def Set_Diff_Update(set_name):
    temp_set = set(map(int, input().split()))
    set_name.difference_update(temp_set)
    return set_name

def Set_Int_Update(set_name):
    temp_set = set(map(int, input().split()))
    set_name.intersection_update(temp_set)
    return set_name

a = int(input())
a_set = set(map(int, input().split()))

Num_Ops=int(input())

for i in range(Num_Ops):
    command_input=input().split()
    
    if(command_input[0]=='intersection_update'):
        Set_Int_Update(a_set)
       
    
    elif(command_input[0]=='update'):
        Set_Update(a_set)
        
        
    elif(command_input[0]=='symmetric_difference_update'):
        Set_SymDiff_Update(a_set)
        
    
    elif(command_input[0]=='difference_update'):
        Set_Diff_Update(a_set)
        

print(sum(a_set))
        