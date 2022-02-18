import decimal


INF = 10 ** 9

def fib(n):
    decimal.getcontext().prec = 10 ** 18
    root_5 = decimal.Decimal(5).sqrt()
    phi = ((1 + root_5) / 2)
    a = ((phi ** n) - ((-phi) ** -n)) / root_5
    return round(a) % INF


n = int(input())
print(fib(n))
