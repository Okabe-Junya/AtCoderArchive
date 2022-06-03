import heapq

N, K = map(int, input().split())

L = []
for _ in range(N):
    L.append(list(map(int, input().split())))

ans = 0
for _ in range(K):
    print(L)
    tmp = heapq.heappop(L)
    ans += tmp[0]
    tmp[0] += tmp[1]
    heapq.heappush(L, tmp)
print(ans)