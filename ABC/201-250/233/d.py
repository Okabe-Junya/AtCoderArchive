N, K = map(int, input().split())
A = list(map(int, input().split()))
A_sum = [0] * (N)
for i in range(N):
    A_sum[i] = A_sum[i - 1] + A[i]
    
print(A_sum)