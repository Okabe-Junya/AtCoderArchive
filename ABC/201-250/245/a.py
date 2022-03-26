A, B, C, D = map(int, input().split())
T = str(A) + str(B)
Ao = str(C) + str(D)
if T <= Ao:
    print("Takahashi")
else:
    print("Aoki")