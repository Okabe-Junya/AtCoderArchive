D = int(input())
N = int(input())
ans_list = [0] * (D + 1)

for _ in range(N):
    l, r = map(int, input().split())
    ans_list[l - 1] += 1
    ans_list[r] -= 1

ans = 0
for i in range(D):
    ans += ans_list[i]
    print(ans)
