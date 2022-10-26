Q = int(input())
s = set()
for _ in range(Q):
    query = list(input().split())
    if query[0] == "1":
        s.add(int(query[1]))
    elif query[0] == "2":
        s.discard(int(query[1]))
    else:
        ans = float('inf')
        for i in s:
            if i >= int(query[1]):
                ans = min(ans, i)
        print(ans if ans != float('inf') else -1)
