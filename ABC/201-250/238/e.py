import numpy as np

N, Q = map(int, input().split())
if N <= Q:
    print("Yes")
    exit()
l = [0 for _ in range(N)]
for i in range(Q):
    a, b = map(int, input().split())
    l[a-1:b] += np.ones(b-a+1)
    
for i in range(N):
    l[i] = int(l[i])
    if l[i] == 0:
        print("No")
        exit()

for i in range(N - 1):
    if l[i + 1] - l[i] % 2 == 1:
        print("No")
        exit()
print("Yes")