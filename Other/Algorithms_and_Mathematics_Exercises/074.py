N = int(input())
A = list(map(int, input().split()))
ans = 0

for i in range(1, N):
    ans += A[i] * i
    ans -= A[N - i - 1] * i
    
print(ans)