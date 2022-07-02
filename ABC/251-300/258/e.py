N, Q, X = map(int, input().split())
W = list(map(int, input().split()))

l = []
cnt = 0
tmp_sum = 0
p = -1
while True:
    p += 1
    if p == N:
        p = 0
    cnt += 1
    tmp_sum += W[p]
    if tmp_sum >= X:
        l.append(cnt)
        if p == N - 1:
            break
        tmp_sum = 0
        cnt = 0
        continue
print(l)

for _ in range(Q):
    K = int(input())
    