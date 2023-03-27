import time

start_time = time.time()
N, M, D, K = map(int, input().split())
G = []
for _ in range(M):
    u, v, _ = map(int, input().split())
    u, v = u - 1, v - 1
    G.append((u, v))

# 読み飛ばす
# ビジュアライザーのための入力
for _ in range(N):
    x, y = map(int, input().split())

ans = [-1] * M
tmp = 1
tmp_set = set()
kcycle = 0
cnt = 0
p = 0
flag = False
while cnt < M:
    tmp_time = time.time()
    if tmp_time - start_time > 5.0:
        flag = True
        break
    if kcycle == K:
        tmp += 1
        kcycle = 0
        tmp_set = set()
    if ((G[p][0] not in tmp_set) or (G[p][1] not in tmp_set)) and (ans[p] == -1):
        ans[p] = tmp
        tmp_set.add(G[p][0])
        tmp_set.add(G[p][1])
        cnt += 1
        kcycle += 1
    p += 1
    if p == M:
        p = 0
if flag:
    tmp = D
    cnt = 0
    for i in range(M):
        if ans[i] == -1:
            ans[i] = tmp
            cnt += 1
            if cnt == K:
                tmp -= 1
                cnt = 0
print(*ans)
