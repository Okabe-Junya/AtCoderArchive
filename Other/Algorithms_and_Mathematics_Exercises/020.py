n = int(input())
a = list(map(int, input().split()))

ans = 0
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            for l in range(k + 1, n):
                for m in range(l + 1, n):
                    tmp = a[i] + a[j] + a[k] + a[l] + a[m]
                    if tmp == 1000:
                        ans += 1
print(ans)