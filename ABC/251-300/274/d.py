N, x, y = map(int, input().split())
A = list(map(int, input().split()))

Aeven = []
Aodd = []
for i in range(N):
    if i == 0:
        x -= A[i]
        continue
    if i % 2 == 0:
        Aeven.append(A[i])
    else:
        Aodd.append(A[i])

if x < 0:
    x = -x
if y < 0:
    y = -y


def solve(A: list, x: int):
    # A の要素の足し引きで x にできるか
    dp = [[False] * (2 * 10**4 + 1) for _ in range(len(A) + 1)]
    dp[0][10**4] = True
    for i in range(len(A)):
        for j in range(2 * 10**4 + 1):
            if dp[i][j]:
                dp[i + 1][j + A[i]] = True
                dp[i + 1][j - A[i]] = True
    return dp[len(A)][x + 10**4]


xcan = solve(Aeven, x)
ycan = solve(Aodd, y)
if xcan and ycan:
    print("Yes")
else:
    print("No")
