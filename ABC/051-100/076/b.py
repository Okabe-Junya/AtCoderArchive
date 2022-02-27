n = int(input())
k = int(input())
cnt = 1
for i in range(n):
    if cnt * 2 < cnt + k:
        cnt *= 2
    else:
        cnt += k
print(cnt)
