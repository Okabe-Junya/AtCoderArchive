n = int(input())
a = list(map(int, input().split()))
a_1 = []
a_2 = []
for i in range(2**(n-1)):
    a_1.append(a[i])
    a_2.append(a[i + 2**(n-1)])
a_1max = max(a_1)
a_2max = max(a_2)
if a_1max > a_2max:
    print(a_2.index(max(a_2)) + 2**(n-1) + 1)
else:
    print(a_1.index(max(a_1))+1)
