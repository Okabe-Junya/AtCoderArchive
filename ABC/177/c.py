n = int(input())
a = list(map(int, input().split()))
l = [0]
ans = 0
for i in range(1, n):
    l.append(l[-1]+a[n-i])
for i in range(n-1):
    ans += a[i] * l[len(l)-i-1]
    ans %= (10**9+7)
print(ans)
