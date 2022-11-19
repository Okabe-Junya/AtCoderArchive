N = int(input())
A = list(map(int, input().split()))
Q = int(input())
all = -1
dict = {}
for _ in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 1:
        all = q[1]
        dict = {}
    elif q[0] == 2:
        if q[1] - 1 in dict:
            dict[q[1] - 1] += q[2]
        else:
            dict[q[1] - 1] = q[2]
    else:
        if all == -1:
            if q[1] - 1 in dict:
                print(A[q[1] - 1] + dict[q[1] - 1])
            else:
                print(A[q[1] - 1])
        else:
            if q[1] - 1 in dict:
                print(all + dict[q[1] - 1])
            else:
                print(all)
