import networkx as nx
# import matplotlib.pyplot as plt
n, m = map(int, input().split())
l = [list(map(int, input().split())) for _ in range(m)]
G = nx.Graph()
G.add_nodes_from([i for i in range(1, n+1)])
G.add_edges_from(l)
for i in range(1, n+1):
    cnt = 0
    tmp = []
    tmp_2 = []
    for j in range(1, n+1):
        if i == j:
            continue
        elif nx.has_path(G, i, j):
            if len(nx.shortest_path(G, i, j)) == 3:
                cnt += 1
    print(cnt)

# nx.draw_networkx(G)
# plt.show()
