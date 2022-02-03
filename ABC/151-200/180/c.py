import math
n = int(input())
sqrtn = math.sqrt(n)
floorn = math.floor(sqrtn)
cnt = 1
nlist = []
while cnt <= floorn:
    if n % cnt == 0:
        nlist.append(cnt)
    cnt += 1
nlist_r = reversed(nlist)
for i in nlist_r:
    nlist.append(n // i)
nums = list(dict.fromkeys(nlist))
for a in nums:
    print(a)
