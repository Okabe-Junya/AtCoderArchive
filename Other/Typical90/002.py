# 002
from itertools import product
n = int(input())
x = '('
y = ')'
l = []
if n % 2 == 0:
    p = product([0,1], repeat = n)
    for i in p:
        zero = 0
        one = 0
        for j in i:
            if j == 0:
                zero += 1
            else:
                one += 1
            if one > zero:
                break
        else:
            if one == zero:
                l.append(i)
        
    for k in l:
        for j in k:
            if j == 0:
                print(x,end='')
            else:
                print(y,end='')
        print('')

            
else:
    print('')