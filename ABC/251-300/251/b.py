from itertools import combinations as cmb

N, W = map(int, input().split())
A = list(map(int, input().split()))
ans = set()

for i in range(N):
    if A[i] <= W:
        ans.add(A[i])

if N < 2:
    print(len(ans))
    exit()
for i in cmb(A, 2):
    if i[0] + i[1] <= W:
        ans.add(i[0] + i[1])

if N < 3:
    print(len(ans))
    exit()
for i in cmb(A, 3):
    if i[0] + i[1] + i[2] <= W:
        ans.add(i[0] + i[1] + i[2])

print(len(ans))