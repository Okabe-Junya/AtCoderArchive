N = int(input())
A = list(map(int, input().split()))
for i in range(N):
    A[i] %= 100
dict = {}
for i in range(N):
    if A[i] in dict:
        dict[A[i]] += 1
    else:
        dict[A[i]] = 1

ans = 0
for i in range(N):
    dict[A[i]] = max(0, dict[A[i]] - 1)
    if (100 - A[i]) % 100 in dict:
        ans += dict[(100 - A[i]) % 100]
print(ans)
