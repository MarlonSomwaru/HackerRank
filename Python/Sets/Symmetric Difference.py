# Author: Marlon Somwaru
# Website: MarlonSomwaru.com
# Github: https://github.com/msomwaru13
# HackerRank: https://www.hackerrank.com/MarlonS

m = int(input())
m_set = set(map(int, input().split()))

n = int(input())
n_set = set(map(int, input().split()))

final_set1 = m_set.difference(n_set)
final_set2 = n_set.difference(m_set)
final_set = final_set1.union(final_set2)

final_set = list(final_set)
final_set.sort()
for i in range(len(final_set)):
    print(final_set[i])