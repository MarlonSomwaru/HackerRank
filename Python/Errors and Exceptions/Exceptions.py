T=int(input()) # Number of Test cases

for i in range(T):
    x,y=input().split()
    
    try:
        print(int(x)//int(y))
    except ZeroDivisionError as e:
        print("Error Code:",e)
    except ValueError as f:
        print("Error Code:",f)