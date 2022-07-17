from collections import deque

N, X, Y, Z = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

Al = {}
Bl = {}
Cl = {}
for i in range(N):
    if A[i] not in Al:
        Al[A[i]] = [i]
    else:
        Al[A[i]].append(i)
    if B[i] not in Bl:
        Bl[B[i]] = [i]
    else:
        Bl[B[i]].append(i)
    if A[i] + B[i] not in Cl:
        Cl[A[i] + B[i]] = [i]
    else:
        Cl[A[i] + B[i]].append(i)

Al = sorted(Al.items(), reverse=True)
Bl = sorted(Bl.items(), reverse=True)
Cl = sorted(Cl.items(), reverse=True)

A = deque()
B = deque()
C = deque()
for i in Al:
    for j in i[1]:
        A.append(j)
for i in Bl:
    for j in i[1]:
        B.append(j)
for i in Cl:
    for j in i[1]:
        C.append(j)

ans = set()
for i in range(X):
    ans.add(A[i])

i = 0
while i < Y:
    tmp = B.popleft()
    if tmp in ans:
        continue
    ans.add(tmp)
    i += 1

i = 0        
while i < Z:
    tmp = C.popleft()
    if tmp in ans:
        continue
    ans.add(tmp)
    i += 1
ans = sorted(list(ans))
for i in ans:
    print(i + 1)