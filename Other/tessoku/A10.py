N = int(input())
A = list(map(int, input().split()))
D = int(input())
Amaxl = [0] * N
Amaxr = [0] * N
Amaxl[0] = A[0]
Amaxr[-1] = A[-1]
for i in range(1, N):
    Amaxl[i] = max(Amaxl[i - 1], A[i])
    Amaxr[-i - 1] = max(Amaxr[-i], A[-i - 1])

for _ in range(D):
    L, R = map(int, input().split())
    print(max(Amaxl[L - 2], Amaxr[R]))
