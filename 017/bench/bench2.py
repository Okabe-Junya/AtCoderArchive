from random import choice


N, M, D, K = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(M):
    u, v, w = map(int, input().split())
    u, v = u - 1, v - 1
    G[u].append((v, w))
    G[v].append((u, w))

num_set = set()
num_dict = {}
for i in range(1, D + 1):
    num_dict[i] = 0
    num_set.add(i)

# 読み飛ばす
# ビジュアライザーのための入力
for _ in range(N):
    x, y = map(int, input().split())

ans = [-1] * M
for i in range(M):
    ans[i] = choice(list(num_set))
    num_dict[ans[i]] += 1
    if num_dict[ans[i]] == K:
        num_set.remove(ans[i])

print(*ans)
