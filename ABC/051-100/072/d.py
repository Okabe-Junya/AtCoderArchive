N = int(input())
p = list(map(int, input().split()))
ans = 0

for i in range(N - 1):
    if p[i] == i + 1:
        p[i], p[i + 1] = p[i + 1], p[i]
        ans += 1

if p[-1] == N or p[-2] == N - 1:
    ans += 1
print(ans)