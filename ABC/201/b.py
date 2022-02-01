n = int(input())
a = [list(input().split()) for i in range(n)]
for i in a:
    i[1] = int(i[1])
li = sorted(a, reverse=True, key=lambda x: x[1])
print(li[1][0])
