import sys
import math

val = int(input())
n = int(input())

next = {}
for i in range (n-1):
    last = {val: n}
    val = n - next.get(val, n)
    next.update(last)
    n += 1

print(val)