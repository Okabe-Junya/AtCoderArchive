import sys

def base_n(num_10, n=3):  # num_10: 10進数, n: 基数
    if num_10 == 0:
        return 0
    str_n = ''
    while num_10: # num_10 != 0
        if num_10 % n >= 10:
            return -1
        str_n += str(num_10 % n)
        num_10 //= n
    return int(str_n[::-1])

dic = {"0": 3, "1": 5, "2": 7}

n = int(input())
if n < 100:
    print(0)
    sys.exit()

l = []
for i in range(3, 10):
    for j in range(3 ** i):
        res = base_n(j)
        tmp = list(str(res).zfill(i))
        num = ''
        for k in tmp:
            num += str(dic[k])
        if len(set(tmp)) == 3:
            l.append(int(num))
l.sort()
ans = 0
for i in l:
    if i > n:
        break
    ans += 1
print(ans)