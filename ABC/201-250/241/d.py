import bisect

def lower_bound(num_list, ky):
    pl = bisect.bisect_left(num_list, ky)
    pr = bisect.bisect_right(num_list, ky)
    return pl, pr

Q = int(input())
A = [0]
for _ in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 1:
        pl, _ = lower_bound(A, q[1])
        A.insert(pl, q[1])
        #print(A)
    
    if q[0] == 2:
        pl, _ = lower_bound(A, q[1])
        if pl - q[2] > 0:
            print(A[pl - q[2]])
        else:
            print(-1)
    
    if q[0] == 3:
        _, pr = lower_bound(A, q[1])
        if pr + q[2] - 1 >= len(A):
            print(-1)
        else:
            print(A[pr + q[2] - 1])