n, k = map(int, input().split())
a = list(map(int, input().split()))
l = [0]
ans = 0
for i in range(n):
    l.append(l[-1] + a[i])
for i in range(n - k + 1):
    ans += l[i + k] - l[i]
print(ans)
