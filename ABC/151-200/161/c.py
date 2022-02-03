n, k = map(int,input().split())
ans = n % k
if abs(ans - k) < abs(ans):
    ans = abs(ans - k)
print(ans)