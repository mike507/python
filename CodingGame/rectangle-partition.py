import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

w, h, count_x, count_y = [int(i) for i in input().split()]
x = [0]
x[1:] = [int(i) for i in input().split()]
y = [0]
y[1:] = [int(i) for i in input().split()]

x.append(w)
y.append(h)

#print(x)
#print(y)


sizex = [x[j]-x[i] for i in range(count_x+2) for j in range(count_x+2) if j>i]
sizey = [y[j]-y[i] for i in range(count_y+2) for j in range(count_y+2) if j>i]
#print(sizex)
#print(sizey)

test = lambda x : 1 if x[0]==x[1] else 0
# res = [test(sizex[i],sizey(j)) for i in range(len(sizex)) for j in range(len(sizey)) ]
print([sizex[i] for i in range(len(sizex))])
print([sizey[i] for i in range(len(sizey))])

genx = ([sizex[i] for i in range(len(sizex))])
geny = ([sizey[i] for i in range(len(sizey))])

# res = list(map(test, (sizex[i] for i in range(len(sizex))), (sizey[j] for j in range(len(sizey)))))
# res = list(map(test,sizey,sizey))
pairs = [ (sizex[i], sizey[j]) for i in range(len(sizex)) for j in range(len(sizey)) ]
print(pairs)

# res = list(map(test, (pairs[i] for i in range(len(pairs)))))
# print(res)

print(res.count(1))
# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)


