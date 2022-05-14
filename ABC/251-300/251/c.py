N = int(input())

tmp_set = set()
ans = 0
max_tmp = 0
for i in range(N):
    S, T = input().split()
    T = int(T)
    if S in tmp_set:
        continue
    else:
        tmp_set.add(S)
        if max_tmp < T:
            max_tmp = T
            ans = i + 1
print(ans)