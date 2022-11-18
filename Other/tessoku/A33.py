N = int(input())
A = list(map(int, input().split()))

xor = 0
for i in range(N):
    xor ^= A[i]

if xor != 0:
    print("First")
else:
    print("Second")
