from decimal import Decimal, ROUND_HALF_UP

A, B = map(int, input().split())
S = B / A
ans = Decimal(str(S)).quantize(Decimal('0.001'), rounding=ROUND_HALF_UP)
print(str(ans).zfill(4))
