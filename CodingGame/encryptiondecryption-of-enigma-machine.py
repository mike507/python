import sys
import math

operation = input()
nb = int(input())

rotor = ['ABCDEFGHIJKLMNOPQRSTUVWXYZ']

for i in range(3):
    r = input()
    rotor.append(r)
message = input()

len = message.__len__()
nbchar = rotor[0].__len__()

if( operation.upper() == 'ENCODE'):
    str = ""
    for i in range(len):
        k = (rotor[0].find(message[i]) + nb + i + nbchar) % nbchar 
        crt = rotor[0][k]
        str += crt
    shiftmsg = str

    for j in range(3):
        str = "" 
        for i in range(len):
            k = rotor[0].find(shiftmsg[i])
            crt = rotor[j+1][k]
            str += crt
        shiftmsg = str
    print(shiftmsg)

if( operation.upper() == 'DECODE'):
    for j in range(3, 0, -1):
        str = "" 
        for i in range(len):
            crt = rotor[j].find(message[i])
            str += rotor[0][crt]
        message = str

    str = ""
    for i in range(len):
        k = (rotor[0].find(message[i]) - nb - i + nbchar) % nbchar 
        crt = rotor[0][k]
        str += crt
    message = str

    print(message)
