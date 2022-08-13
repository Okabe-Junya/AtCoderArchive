N = int(input())
P = list(map(int, input().split()))
dict = {}
for p in range(len(P)):
    dict[p + 2] = P[p]
ans = 0
p = N
while p != 1:
    ans += 1
    p = dict[p]
print(ans)