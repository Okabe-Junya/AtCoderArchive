from heapq import heappop, heappush


N, D = map(int, input().split())
dict = {}
for _ in range(N):
    X, Y = map(int, input().split())
    Y = -Y
    if X in dict:
        dict[X].append(Y)
    else:
        dict[X] = [Y]

tmp = []
ans = 0
for d in range(1, D + 1):
    if d in dict:
        for y in dict[d]:
            heappush(tmp, y)
    if tmp:
        ans += heappop(tmp)
print(-ans)
