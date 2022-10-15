from decimal import Decimal, ROUND_HALF_UP

X, K = map(int, input().split())

for i in range(1, K + 1):
    X = Decimal(str(X))
    X = X.quantize(Decimal(f'1E{i}'), rounding=ROUND_HALF_UP)
    X = int(X)
print(X)
