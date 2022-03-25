from collections import deque

INF = 998244353

N, M, K, S, T, X = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)

queue = deque([S - 1])
d = [-1] * N
d[S - 1] = 0

def bfs(G, d, queue):
    """bfs: breadth-first search
    Args:
        G (list): G[i] is the list of neighbors of node i.
        d (list): d[i] is the distance from the source to node i.
        queue (collections.deque): queue of nodes to visit next.
    Returns:
        list: d[i] for all nodes i in the breadth-first order.
            (if node i has no outgoing edges, then d[i] will be -1.)
    """
    
    while queue:
        next = queue.popleft()
        for node in G[next]:
            if d[node] == -1:
                d[node] = d[next] + 1
                queue.append(node)
    return 

bfs(G, d, queue)
print(d)