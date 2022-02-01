n = int(input())
n_list = list(map(int, input().split()))
n_dict = {}
cnt = 0
for j in range(2, 1000):
    for i in n_list:
        if i % j == 0:
            cnt += 1
    n_dict[j] = cnt
    cnt = 0
max_key = max(n_dict, key=n_dict.get)
print(max_key)
