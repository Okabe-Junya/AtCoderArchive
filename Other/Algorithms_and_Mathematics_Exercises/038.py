n, q = map(int, input().split())
a = list(map(int, input().split()))
a_sum = [0] * (n + 1)
a_sum[1] = a[0]
for i in range(1, n + 1):
    a_sum[i] = a_sum[i - 1] + a[i - 1]
# print(a_sum)

for _ in range(q):
    l, r = map(int, input().split())
    print(a_sum[r] - a_sum[l - 1])