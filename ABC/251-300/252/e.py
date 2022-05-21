from heapq import heappush, heappop

N, M = map(int, input().split())
G = []
for i in range(M):
    a, b, c = map(int, input().split())
    G.append((i, a, b, c))
G.sort(key=lambda x: x[2])
print(G)
tree = []
for k in range(M):
    tmp_tree = []