N, Q = map(int, input().split())
ff = {}
for _ in range(Q):
    T, A, B = map(int, input().split())
    if T == 1:
        if A - 1 in ff:
            ff[A - 1].add(B - 1)
        else:
            ff[A - 1] = set([B - 1])
    elif T == 2:
        if A - 1 in ff:
            ff[A - 1].discard(B - 1)
    elif T == 3:
        if (A - 1 not in ff) or (B - 1 not in ff):
            print("No")
            continue
        if (A - 1 in ff[B - 1]) and (B - 1 in ff[A - 1]):
            print("Yes")
        else:
            print("No")
