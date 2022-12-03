H, W = map(int, input().split())
ans = 0
for _ in range(H):
    L = list(input())
    ans += L.count('#')
print(ans)
