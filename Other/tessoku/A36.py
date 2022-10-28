N, K = map(int, input().split())
m = 2 * (N - 1)
if K > m and (K - m) % 2 == 0:
    print("Yes")
else:
    print("No")
