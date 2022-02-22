n = int(input())
a = list(map(int, input().split()))
cnt = 0
tmp = 0
ans = 0
cnt_sum = 0
for i in range(n):
    ans += 1
    if a[i] == tmp:
        cnt += 1
        if tmp == cnt:
            cnt_sum += cnt
            ans -= cnt
            if i - cnt_sum >= 0:
                tmp = a[i - cnt_sum]
            else:
                tmp = 0
            #print("tmp:", tmp)
            cnt = 1
            while (i - cnt_sum - cnt >= 0) and (a[i - cnt_sum - cnt] == tmp):
                cnt += 1
            #print("cnt:", cnt)
    else:
        cnt = 1
        tmp = a[i]
    print(ans)