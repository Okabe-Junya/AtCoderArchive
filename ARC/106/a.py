import math
n = int(input())
l = [-1]
t = 1
while t <= 10 ** 18:
    t *= 3
    l.append(t)
b = round(math.log(n, 5))
for i in range(1, int(b)+1):
    a = n - 5 ** i
    if a in l:
        print(l.index(a), i)
        break
else:
    print(-1)
