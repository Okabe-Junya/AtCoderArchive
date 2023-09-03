from itertools import combinations


N, K = map(int, input().split())
INF = 10**9 + 7
ans = 0
pattern = set()
if N <= 10**5:
    for i in combinations(range(N), K):
        if i in pattern:
            continue
        ans += 1
        pattern.add(i)
elif K == 3:
    print(ans)
else:
    print(ans)
