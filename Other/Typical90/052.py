n = int(input())
a = [list(map(int,input().split())) for i in range(n)]
ans = 1
INF = 10 ** 9 + 7
for i in a:
    ans *= sum(i)
print(ans % INF)