N, M = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)

for i in range(N):
    print(len(G[i]), end=' ')
    L = sorted(G[i])
    for j in range(len(L)):
        print(L[j] + 1, end=' ')
    print()
