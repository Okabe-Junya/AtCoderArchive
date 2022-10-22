H, W = map(int, input().split())
ans_list = [0] * W
for _ in range(H):
    A = list(input())
    for i in range(W):
        if A[i] == '#':
            ans_list[i] += 1

print(*ans_list)
