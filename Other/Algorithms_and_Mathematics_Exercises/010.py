n = int(input())


def f(n):
    if n == 1:
        return n
    else:
        return n * f(n - 1)


print(f(n))