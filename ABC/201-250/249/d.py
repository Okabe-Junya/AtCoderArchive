def make_divistors(n):
    lower, upper = [], []
    i = 1
    while i * i <= n:
        if n % i == 0:
            lower.append(i)
            upper.append(n // i)
        i += 1
    return lower, upper

N = int(input())
A = list(map(int, input().split()))
A.sort()
ans = 0
dict = {}
for i in range(N):
    if A[i] not in dict:
        dict[A[i]] = 1
    else:
        dict[A[i]] += 1


for i in range(N):
    res1, res2 = make_divistors(A[i])
    for j in range(len(res1)):
        if res1[j] in dict and res2[j] in dict:
            if res1[j] != res2[j]:
                ans += dict[res1[j]] * (dict[res2[j]]) * 2
            else:
                ans += dict[res1[j]] * dict[res1[j]]
print(ans)