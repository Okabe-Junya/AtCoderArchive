n, k = map(int, input().split())
A = list(map(int, input().split()))

memo = [[False, 0] for _ in range(n)]
tmp = 0
ans = 0
for i in range(k):
    tmp = ans % n
    if not memo[tmp][0]:
        memo[tmp][0] = True
        memo[tmp][1] = i + 1
        ans += A[tmp]
    else:
        cycle = [False] * n
        
        break    
print(ans)
print(memo)