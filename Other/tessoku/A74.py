N = int(input())
Px = [0] * N
Py = [0] * N

dx = 0
dy = 0

for i in range(N):
    P = list(map(int, input().split()))
    for j in range(N):
        if P[j] != 0:
            Px[P[j] - 1] = i
            Py[P[j] - 1] = j

for i in range(N - 1):
    for j in range(i + 1, N):
        if Px[i] > Px[j]:
            dx += 1
        if Py[i] > Py[j]:
            dy += 1

print(dx + dy)
