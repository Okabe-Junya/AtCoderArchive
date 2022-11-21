M, eps = input().split()
M = int(M)
eps = float(eps)
N = M
print(N)
length = N * (N - 1) // 2
for i in range(M):
    print("1" * i + "0" * (length - i))


for _ in range(100):
    H = input()
    cnt = H.count("1")
    print(min(cnt, M - 1))
