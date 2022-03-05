n, k = map(int, input().split())
ans = 0
for i in range(2, 2*n+1):
    c = n - abs(n+1-i)
    if i - k < 2 or i - k > 2 * n:
        continue
    else:
        d = n - abs(n+1-(i-k))
    ans += c * d
print(ans)
