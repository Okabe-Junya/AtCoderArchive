Q = int(input())
dict = {}
for _ in range(Q):
    query = list(input().split())
    if query[0] == "1":
        dict[query[1]] = query[2]
    elif query[0] == "2":
        print(dict[query[1]])
