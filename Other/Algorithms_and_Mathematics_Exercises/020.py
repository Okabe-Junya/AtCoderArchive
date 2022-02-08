n = int(input())
f(n)

def f(n):
    if n == 1:
        print(n)
    return n * f(n - 1)