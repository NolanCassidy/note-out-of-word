import sys
from collections import *

def problem1(magazine, note):
    mdict = {}
    ndict = {}

    for m in magazine:
        mdict[m]=0
    for n in note:
        ndict[n]=0

    for m in magazine:
        mdict[m]=mdict[m]+1
    for n in note:
        ndict[n]=ndict[n]+1

    for k in ndict:
        if(not(k in mdict) or ndict[k]>mdict[k]):
            return False
    return True

def driver():
    f = open(sys.argv[1])
    mlen,nlen = map(int,f.readline().strip().split(' '))
    magazine = f.readline().strip().split(' ')
    note = f.readline().strip().split(' ')

    check = problem1(magazine,note)
    if(check==True):
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    driver()
