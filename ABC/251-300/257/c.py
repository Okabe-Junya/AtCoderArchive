from bisect import bisect_right

N = int(input())
S = input()
W = list(map(int, input().split()))
adult = []
child = []
for i in range(N):
    if S[i] == "1":
        adult.append(W[i])
    else:
        child.append(W[i])

adult.sort()
child.sort()
if len(child) == 0 or len(adult) == 0:
    print(N)
    exit()

ans = 0
for i in range(len(adult)):
    p = bisect_right(child, adult[i] - 0.1)
    tmp_ans = p + (len(adult) - i)
    if tmp_ans > ans:
        ans = tmp_ans

print(ans)