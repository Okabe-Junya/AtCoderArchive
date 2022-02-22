n = int(input())
a = list(map(int, input().split()))
l = []
tmp = 0
cnt = 0
for i in range(n):
    tmp = a[i]
    l.append(tmp)
    if len(l) >= tmp:
        for i in range(tmp):
            if l[len(l) - i - 1] != tmp:
                break
        else:
            for i in range(tmp):
                l.pop()
    print(len(l))