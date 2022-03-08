N, M = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(M):
    A, B = map(int, input().split())
    G[A - 1].append(B - 1)
    G[B - 1].append(A - 1)

color = [-1] * N


def dfs(tmp_node, G, cur):
    color[tmp_node] = cur
    for next in G[tmp_node]:
        if color[next] != -1:
            if color[next] == cur:
                return False
        else:
            return dfs(next, G, 1 - cur)
    return True


#print(dfs(0, G, 1))
#print(color)

if dfs(0, G, 1):
    print('Yes')
else:
    print('No')
