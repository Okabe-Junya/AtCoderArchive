n = int(input())
s = list(input())
q = int(input())
k = 0
for _ in range(q):
    t, a, b = map(int, input().split())
    if t == 1:
        s[(a-1+k*n) % (2*n)], s[(b-1+k*n) %
                                (2*n)] = s[(b-1+k*n) % (2*n)], s[(a-1+k*n) % (2*n)]
    else:
        k += 1
if k % 2 == 1:
    for i in range(2*n):
        print(s[(n+i) % (2*n)], end='')
else:
    for i in range(2*n):
        print(s[i], end='')
