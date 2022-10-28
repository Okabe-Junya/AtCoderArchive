N = int(input())
tol = 1e-3
pl = 0
pr = 10**5


def f(x):
    return x**3 + x


while pl < pr:
    pm = (pl + pr) / 2
    if f(pm) < N:
        pl = pm
    else:
        pr = pm
    if abs(f(pm) - N) < tol:
        break

print(pm)
