from itertools import product
a = list(map(int, input().split()))
s = sum(a)
l = product([0, 1], repeat=4)
for i in l:
    tmp = 0
    for j in range(4):
        if i[j] == 1:
            tmp += a[j]
        if tmp == s - tmp:
            print('Yes')
            exit()
else:
    print('No')
