# Author: Marlon Somwaru
# Website: MarlonSomwaru.com
# Github: https://github.com/msomwaru13
# HackerRank: https://www.hackerrank.com/MarlonS

def Second_Element(elem):
    return elem[1]

if __name__ == '__main__':
###### Initial Inputs ######   
    student_list=[] # List of students
    
    for i in range(int(input())):
        name = input()
        score = float(input())
        student_list.append([name, score])

##### Deal with scores ######
    student_list.sort(key=Second_Element) # sort list by grades
    
    score_list = [] # List of just scores
    
    for j in range(len(student_list)): # Accumulate list of scores
        score_list.append(Second_Element(student_list[j]))
    
    score_list=set(score_list) #Sets only contain unique values
    score_list=list(score_list) #Convert back to extract value
    score_list.sort()
    second_lowest=score_list[1] #Second lowest unique score
    
    final_list_names=[]
    
    for k in range(len(student_list)):
        if(Second_Element(student_list[k])==second_lowest):
            final_list_names.append(student_list[k][0])
    
    final_list_names=sorted(final_list_names)
    
    for l in range(len(final_list_names)):
        print(final_list_names[l])