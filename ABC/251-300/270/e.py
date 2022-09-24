N, K = map(int, input().split())
A = list(map(int, input().split()))

tmp = K // N
for i in range(N):
    A[i] -= tmp

for i in range(K % N):
    A[i] -= 1

s = 0
for i in range(N):
    if A[i] < 0:
        s -= A[i]
        A[i] = 0

while s > 0:
    for i in range(N):
        if A[i] > 0:
            A[i] -= N // K
            s -= 1
            if s == 0:
                break
print(*A)
