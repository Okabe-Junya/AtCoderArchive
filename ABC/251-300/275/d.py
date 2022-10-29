import sys

sys.setrecursionlimit(10**5)

N = int(input())
dict = {0: 1}


def f(x):
    if x in dict:
        return dict[x]
    else:
        dict[x] = f(x // 2) + f(x // 3)
        return dict[x]


print(f(N))
