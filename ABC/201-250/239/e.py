import sys


def LI():
    return [int(x) for x in sys.stdin.readline().split()]


n, q = LI()
x = list(map(int, sys.stdin.readline().split()))

v = [[] for _ in range(n)]
for i in range(n - 1):
    a, b = LI()
    a -= 1  # listのindex参照をそのまま使いたいので頂点id(1から始まっている)を-1しておく
    b -= 1  # aと同様
    v[a].append(b)
    v[b].append(a)

seen = [False] * (n)
seen[0] = True
l = []
start = [0] * (n)
end = [0] * (n)
cnt = 0
def rec(i, cnt):
    seen[i] = True
    l.append(i)
    start[i] = cnt
    cnt += 1
    for node in v[i]:
        if seen[node] == False:
            rec(node, cnt)
    l.append(i)
    end[i] = cnt
    cnt += 1
#print(v)
rec(0, cnt)
print(l)
print(start)
print(end)

for _ in range(q):
    v, k = LI()