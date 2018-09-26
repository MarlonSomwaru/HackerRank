# Author: Marlon Somwaru
# Website: MarlonSomwaru.com
# Github: https://github.com/msomwaru13
# HackerRank: https://www.hackerrank.com/MarlonS

n = int(input())
eng_news = set(map(int, input().split()))

b = int(input())
french_news = set(map(int, input().split()))

final_set=eng_news.union(french_news)
final_set=list(final_set)
print(len(final_set))