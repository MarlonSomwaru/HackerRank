# Author: Marlon Somwaru
# Website: MarlonSomwaru.com
# Github: https://github.com/msomwaru13
# HackerRank: https://www.hackerrank.com/MarlonS

good_count = 0
sad_count = 0

n,m = map(int, input().split())

check_array = list(map(int, input().split()))

good_set = set(map(int, input().split()))
bad_set = set(map(int, input().split()))

for i in check_array:
    if(i in good_set):
        good_count +=1

for i in check_array:
    if(i in bad_set):
        sad_count +=1
print(good_count-sad_count)