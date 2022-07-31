N, M = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    G[a-1].append(b-1)
    G[b-1].append(a-1)

ans = 0
for i in range(N-2):
    for j in range(i+1,N-1):
        for k in range(j+1,N):
            if i in G[j] and j in G[k] and k in G[i]:
                ans += 1
print(ans)