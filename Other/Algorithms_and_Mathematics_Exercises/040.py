n = int(input())
a = list(map(int, input().split()))
a_sum = [0] * (n)
a_sum[0] = 0
for i in range(1, n):
    a_sum[i] = a_sum[i - 1] + a[i - 1]
m = int(input())
# print(a_sum)
ans = 0
b1 = int(input())
for _ in range(m - 1):
    b = int(input())
    ans += abs(a_sum[b - 1] - a_sum[b1 - 1])
    b1 = b
    # print(ans)
print(ans)