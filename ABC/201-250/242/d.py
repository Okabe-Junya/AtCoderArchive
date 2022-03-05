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
        x = k - 1 - group * (2 ** t)
    else:
        group = 0
        x = k - 1
    x = str(bin(x)[2:])
    #print(len(x))
    sc = S[group]
    #print(x)
    for char in x:
        if char == "0":
            sc = dict[sc][0]
        else:
            sc = dict[sc][1]
    rest = t - len(x)
    if rest > 0:
        rest %= 3
        for _ in range(rest):
            sc = dict[sc][0]
    print(sc)
    