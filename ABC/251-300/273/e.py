from sys import stdin

A = []
note = {}
Q = int(stdin.readline())
for _ in range(Q):
    L = stdin.readline().split()
    if L[0] == 'ADD':
        A.append(L[1])
    elif L[0] == 'DELETE':
        if len(A) > 0:
            A.pop()
    elif L[0] == 'SAVE':
        note[L[1]] = A[:]
    elif L[0] == 'LOAD':
        if L[1] in note:
            A = note[L[1]][:]
        else:
            A = []
    if len(A) > 0:
        print(A[-1], end=' ')
    else:
        print(-1, end=' ')
print()
