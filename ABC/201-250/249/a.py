A, B, C, D, E, F, X = map(int, input().split())
tsum = 0
asum = 0
for i in range(1, X + 1):
    if 0 < i % (A + C) <= A:
        tsum += B
    if 0 < i % (D + F) <= D:
        asum += E
        

if tsum > asum:
    print("Takahashi")
elif tsum < asum:
    print("Aoki")
else:
    print("Draw")