n = int(input())
a = list(map(int, input().split()))
ans = 0
while True:
    break_flag = False
    for i in range(n):
        if a[i] % 2 == 0:
            a[i] //= 2
        else:
            break_flag = True
            break
    if break_flag:
        break
    ans += 1
print(ans)