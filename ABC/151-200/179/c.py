n = int(input())
idx = 0
for i in range(1, n):
    idx += (n-1)//i
print(idx)
