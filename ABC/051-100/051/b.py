k, s = map(int, input().split())
ans = 0
for i in range(s+1):
    for j in range(s+1-i):
        if i <= k and j <= k and (s-i-j) <= k:
            ans += 1
print(ans)