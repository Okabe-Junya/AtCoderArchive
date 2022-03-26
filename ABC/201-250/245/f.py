import sys

sys.setrecursionlimit(10**6)

N, M = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(M):
    U, V = map(int, input().split())
    G[U - 1].append(V - 1)

ans = [False] * N

def dfs(start, seen):
    # print(seen)
    if start in seen:
        return seen
    seen.append(start)
    for i in G[start]:
        return dfs(i, seen)
    
    
for i in range(N):
    if not ans[i]:
        seen = []
        res = dfs(i, seen)
        if res is not None:
            ans[i] = True
            for j in res:
                ans[j] = True
print(sum(ans))