# Author: Marlon Somwaru
# Website: MarlonSomwaru.com
# Github: https://github.com/msomwaru13
# HackerRank: https://www.hackerrank.com/MarlonS

if __name__ == '__main__':
    xlist = range(int(input()) + 1)
    ylist = range(int(input()) + 1)
    zlist = range(int(input()) + 1)
    n = int(input())
    final_list = [[x,y,z] for x in xlist for y in ylist for z in zlist if x + y + z != n]
    print(final_list)