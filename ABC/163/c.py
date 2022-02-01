n = int(input())
a = list(map(int, input().split()))
l = [0 for _ in range(n)]
for i in a:
    l[i-1] += 1

for j in l:
    print(j)
