List_Count=int(input())
N=list(map(int, input().split()))

Case_1 = all(i>0 for i in N)
str_list = map(str, N)
Case_2 = any(i == i[::-1] for i in str_list)

if(Case_1 and Case_2 == True):
    print(True)
else:
    print(False)