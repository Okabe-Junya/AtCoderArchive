n = int(input())
d = [int(input()) for i in range(n)]
d_list = sorted(d)
a = list(set(d_list))
print(len(a))
