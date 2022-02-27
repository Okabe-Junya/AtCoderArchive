from itertools import permutations
n = int(input())
p = list(map(int, input().split()))
q = list(map(int, input().split()))
l = list(range(1, n + 1))
b = permutations(l, n)
cnt = 0
s = g = 0
for i in b:
    cnt += 1
    if list(i) == p:
        s = cnt
    if list(i) == q:
        g = cnt
print(abs(s - g))
