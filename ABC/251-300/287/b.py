N, M = map(int, input().split())
Nl = []
for _ in range(N):
    Nl.append(input())

Ml = []
for _ in range(M):
    Ml.append(input())

ans = 0
for i in Nl:
    tmp = i[-3:]
    if tmp in Ml:
        ans += 1

print(ans)
