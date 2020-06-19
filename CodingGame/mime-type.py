import sys
import math

n = int(input())  # Number of elements which make up the association table.
q = int(input())  # Number Q of file names to be analyzed.
d = {}

for i in range(n):
    ext, mt = input().split()
    d[ext.upper()] = mt

for i in range(q):
    fname = input()  # One file name per line.
    p = fname.rfind('.')
    if( p == -1):   #not found
        print("UNKNOWN")
    else:
        fext = fname[p+1:].upper()
        try:
            print (d[fext])
        except KeyError:
            print ("UNKNOWN")
