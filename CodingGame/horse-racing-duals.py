import sys
import math

n = int(input())
l = []

for i in range(n):
    pi = int(input())
    l.append(pi)
l.sort()

minval = sys.maxsize

for i in range(n-1):
    crtval = l[i+1] - l[i]
    if(minval > crtval):
        minval = crtval

print(minval)