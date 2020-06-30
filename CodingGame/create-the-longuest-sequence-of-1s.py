b=input().split("0")
maxlen = 0
cur = 0
while cur != -1:
    cur = b.find('0', pos)
    if cur != -1:
        temp = b[:cur] + '1' + b[cur+1:]
        #print(temp)
        l = temp.rsplit('0')
        m = max([len(i) for i in l])
        if m > maxlen:
            maxlen = m
        pos = cur + 1
print(maxlen)

#b=input().split("0")
#print(max(len(b[i])+1+len(b[i+1]) for i in range(len(b)-1)))
