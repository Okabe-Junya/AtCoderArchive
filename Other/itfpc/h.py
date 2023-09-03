N = int(input())
G = [[] for _ in range(N)]
for _ in range(N - 1):
    u, v, _d = map(int, input().split())
    G[u - 1].append(v - 1)
