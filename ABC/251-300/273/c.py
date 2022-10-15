N = int(input())
A = list(map(int, input().split()))

Al = list(set(A))
Al.sort(reverse=True)
d = {}
for a in A:
    if a in d:
        d[a] += 1
    else:
        d[a] = 1

for i in range(N):
    if i < len(Al):
        print(d[Al[i]])
    else:
        print(0)
