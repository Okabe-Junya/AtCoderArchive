k = int(input())
a = 7
for i in range(k):
    if a % k == 0:
        print(i+1)
        break
    else:
        a = int(str(a) + '7') % k
else:
    print(-1)
