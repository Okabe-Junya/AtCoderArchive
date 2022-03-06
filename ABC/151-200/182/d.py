N = int(input())
A = list(map(int, input().split()))
A_sum = [0] * N
for i in range(N):
    A_sum[i] = A_sum[i - 1] + A[i]

ans = [0]
tmp = 0
for i in range(N):
    tmp += A_sum[i]
    ans.append(tmp)
print(max(ans))