N, Q = map(int, input().split())
A = [i + 1 for i in range(N)]
reverse = False
for _ in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 1:
        x, y = q[1] - 1, q[2]
        if reverse:
            A[N - x - 1] = y
        else:
            A[x] = y
    elif q[0] == 2:
        reverse = not reverse
    else:
        x = q[1] - 1
        print(A[N - x - 1] if reverse else A[x])
