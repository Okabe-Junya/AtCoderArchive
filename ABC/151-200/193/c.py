import math
n = int(input())
m_1 = math.sqrt(n)
m = math.floor(m_1)
ans = 0
p = set([])
for i in range(2, m+1):
    if i in p:
        continue
    tmp = math.floor(math.log(n, i))
    ans += tmp - 1
    for j in range(tmp):
        p.add(i ** (j+1))

print(n - ans)
