# Author: Marlon Somwaru
# Website: MarlonSomwaru.com
# Github: https://github.com/msomwaru13
# HackerRank: https://www.hackerrank.com/MarlonS

country_list=[]

for i in range(int(input())):
    country = input()
    country_list.append(country)
    
country_list=set(country_list)
print(len(country_list))