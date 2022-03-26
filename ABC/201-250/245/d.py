import numpy as np

N, M = map(int, input().split())
A = list(map(int, input().split()))
C = list(map(int, input().split()))
A.reverse()
C.reverse()

p = np.poly1d(A)
q = np.poly1d(C)
ans = (q / p)[0]
l = []
for i in ans:
    l.append(int(i))
l.reverse()
for i in l:
    print(i, end=" ")
