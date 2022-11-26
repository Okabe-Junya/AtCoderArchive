from math import sqrt, ceil, floor

A, B = map(int, input().split())


def f(x):
    return A / sqrt(1 + x) + B * x


gl = 0
gr = 10 ** 18

while gr > gl + 0.1:
    g1 = (gl * 2 + gr) / 3
    g2 = (gl + gr * 2) / 3
    if f(g1) > f(g2):
        gl = g1
    else:
        gr = g2

print(min(f(x) for x in range(floor(gl), ceil(gr) + 1)))
