from math import ceil, log2

S = input()
Q = int(input())
ls = len(S)
dict = {"A": "BC", "B": "CA", "C": "AB"}
for _ in range(Q):
    t, k = map(int, input().split())
    if t == 0:
        print(S[k - 1])
        continue
    if t < 60:
        group = (k - 1) // (2 ** t)
        x = k - group * (2 ** t)
    else:
        group = 0
        x = k
    start = S[group]
    print("x", x)
    idx = ceil(log2(x))
    for i in range(idx):
        if x & (1 << i):
            start = dict[start][1]
        else:
            start = dict[start][0]
    print(start)
    rest = x - idx
    print("rest", rest)
        