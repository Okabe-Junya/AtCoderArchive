N, M, Q = map(int, input().split())
imos1 = [0] * M
for _ in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 1:
        imos1[q[1]] += q[3]
        imos1[q[2]] -= q[3]