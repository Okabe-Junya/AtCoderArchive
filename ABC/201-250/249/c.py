N, K = map(int, input().split())
S = []
for _ in range(N):
    S.append(input())
ans = 0
for i in range(2 ** N):
    tmp_ans = 0
    dict = {}
    i = str(bin(i)[2:]).zfill(N)
    for bit in range(len(i)):
        if i[bit] == "1":
            tmp = S[bit]
            for s in tmp:
                if s not in dict:
                    dict[s] = 1
                else:
                    dict[s] += 1
    for key in dict:
        if dict[key] == K:
            tmp_ans += 1
    
    if tmp_ans > ans:
        ans = tmp_ans
print(ans)