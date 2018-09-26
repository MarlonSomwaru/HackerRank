# Author: Marlon Somwaru
# Website: MarlonSomwaru.com
# Github: https://github.com/msomwaru13
# HackerRank: https://www.hackerrank.com/MarlonS

n = int(input())
n_set = set(map(int, input().split()))

b = int(input())
b_set = set(map(int, input().split()))

final_set = n_set.difference(b_set)
final_set = list(final_set)
print(len(final_set))