Q = int(input())
stack = []
for _ in range(Q):
    query = list(input().split())
    if query[0] == "1":
        stack.append(query[1])
    elif query[0] == "2":
        print(stack[-1])
    else:
        stack.pop()
