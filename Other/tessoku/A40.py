N = int(input())
A = list(map(int, input().split()))
dict = {}
for a in A:
    if a in dict:
        dict[a] += 1
    else:
        dict[a] = 1

ans = 0
for d in dict:
    if dict[d] < 3:
        continue
    ans += dict[d] * (dict[d] - 1) * (dict[d] - 2) // 6
print(ans)
