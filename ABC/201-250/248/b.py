ans = 0
A, B, K = map(int, input().split())
if A >= B:
    print(ans)
    exit()
while A < B:
    ans += 1
    A *= K
print(ans)