import math
from decimal import *
n = int(input())
getcontext().prec = 20
i = Decimal(8 * n + 9).sqrt()
print(n+2-int((i+1)/2))
