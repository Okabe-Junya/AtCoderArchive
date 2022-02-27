n = int(input())
a = list(map(int, input().split()))
s = sum(a)
if s % n != 0:
    print(-1)
else:
    ave = s // n
    tmp = 0
    cnt = 0
    for i in range(n):
        tmp += a[i]
        if tmp == (i + 1) * ave:
            cnt += 1
    print(n - cnt)
