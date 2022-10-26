N, M = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)

for i in range(N):
    print(f"{i + 1}:", end=" ")
    print("{", end="")
    for j in range(len(G[i])):
        if j != len(G[i]) - 1:
            print(f"{G[i][j] + 1}, ", end="")
        else:
            print(f"{G[i][j] + 1}", end="")
    print("}")
