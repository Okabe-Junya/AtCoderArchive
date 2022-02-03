n, k = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
tmp = 0
for i in range(n):
    tmp += abs(a[i] - b[i])
if tmp <= k and (k - tmp) % 2 == 0:
    print('Yes')
else:
    print('No')