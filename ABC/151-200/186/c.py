n = int(input())


def for8(x):
    if (int(x/8)):
        return for8(int(x/8))+str(x % 8)
    return str(x % 8)


cnt = 0
for i in range(1, n+1):
    if '7' in str(i):
        cnt += 1
    else:
        a = for8(i)
        if '7' in a:
            cnt += 1
print(n - cnt)
