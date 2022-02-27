n = int(input())
l = list(map(int, input().split()))
a = []
for i in l:
    cnt = 0
    while i % 2 == 0:
        cnt += 1
        i = i // 2
    a.append(cnt)

print(min(a))
