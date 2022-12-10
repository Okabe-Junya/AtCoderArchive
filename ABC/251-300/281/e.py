from heapq import heappush, heappop
from collections import deque

N, M, K = map(int, input().split())
A = list(map(int, input().split()))

# Mこの整数を昇順に並び替えたときの先頭K個の和を求める

queue = deque()
tmp_list = []
for i in range(M):
    tmp_list.append(A[i])

for i in range(N - M):
    ans = -1
    for j in range(K):
        ans = heappop(queue)
        heappush(queue, ans + A[i + M])
    tmp_list.append(ans)
    print(ans, end=' ')
