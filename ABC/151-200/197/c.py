from itertools import product
n = int(input())
x = list(map(int, input().split()))
if n == 1:
    print(x[0])
    exit()
l = []
a = product([0, 1], repeat=n-1)
for i in a:
    tmp = x[0]
    cnt = 0
    for j in range(len(i)):
        if i[j] == 1:
            cnt = cnt ^ tmp
            tmp = x[j+1]
        else:
            tmp = tmp | x[j+1]
    else:
        cnt = cnt ^ tmp
    l.append(cnt)
print(min(l))
