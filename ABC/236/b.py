n = int(input())
a = list(map(int, input().split()))

s = 2 * n * (n + 1)
print(s - sum(a))