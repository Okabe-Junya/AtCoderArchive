a = [int(input()) for i in range(4)]
A = a[0]
B = a[1]
C = a[2]
X = a[3]
idx = 0
for i in range(A+1):
    for j in range(B+1):
        for k in range(C+1):
            if i*500 + j*100 + k*50 == X:
                idx += 1

print(idx)
