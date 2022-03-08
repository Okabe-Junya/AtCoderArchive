INF = 10 ** 9 + 7
N = int(input())
A = list(map(int, input().split()))

weight = [1] * N
for i in range(1, N):
    weight[i] = round(weight[i - 1] * ((N - i) / i))
#print(weight)

ans = 0
for i in range(N):
    ans += A[i] * weight[i]
    ans %= INF
print(ans)