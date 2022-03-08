from collections import deque

n, m = map(int, input().split())
edge = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    edge[a - 1].append(b - 1)
    edge[b - 1].append(a - 1)
# print(edge)

if n == 1:
    print("The graph is connected.")
    exit()

can = [-1] * n
queue = deque([0])

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
    return d

can = bfs(edge, can, queue)

# print(can)
for i in can:
    if i == -1:
        print("The graph is not connected.")
        break
else:
    print("The graph is connected.")
