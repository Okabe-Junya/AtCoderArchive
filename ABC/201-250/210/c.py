from collections import deque

n, k = map(int, input().split())
c = list(map(int, input().split()))
tmp = deque(c[:k])
ans = len(set(tmp))
for i in range(k, n):
    tmp.append(c[i])
    tmp.popleft()
    # print(tmp)
    ans = max(ans, len(set(tmp)))
print(ans)