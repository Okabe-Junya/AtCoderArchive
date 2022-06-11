R, C = map(int, input().split())
L = []
for _ in range(2):
    A, B = map(int, input().split())
    L.append((A, B))
print(L[R - 1][C - 1])