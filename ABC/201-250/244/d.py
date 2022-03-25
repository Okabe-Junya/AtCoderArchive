S1, S2, S3 = input().split()
T1, T2, T3 = input().split()
tmp = 0
if  S1 == T1:
    tmp += 1
if  S2 == T2:
    tmp += 1
if  S3 == T3:
    tmp += 1
if (tmp == 0) or (tmp == 3):
    print("Yes")
else:
    print("No")