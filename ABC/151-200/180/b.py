import math
n = int(input())
x_n = list(map(int, input().split()))
y_n = []
z_n = []
for i in x_n:
    if i < 0:
        i = -i
    y_n.append(i)
    i = i ** 2
    z_n.append(i)
print(sum(y_n))
print(math.sqrt(sum(z_n)))
print(max(y_n))
