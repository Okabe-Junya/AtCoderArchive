import math
a, b, c, d = map(int, input().split())
if a % c == 0:
    a_1 = a // c - 1
else:
    a_1 = a // c
if a % d == 0:
    a_2 = a // d - 1
else:
    a_2 = a // d
b_1 = b // c
b_2 = b // d
c_num = b_1 - a_1
d_num = b_2 - a_2
lcm = c * d // math.gcd(c, d)
if a % lcm == 0:
    a_3 = a // lcm - 1
else:
    a_3 = a // lcm
b_3 = b // lcm
lcm_num = b_3 - a_3
cnt = b - a + 1 - (c_num + d_num - lcm_num)
print(cnt)
