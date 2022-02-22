n = int(input())
a = list(map(int, input().split()))
stack = [[0, 0]]
for i in range(n):
    if a[i] != stack[-1][0]:
        stack.append([a[i], 1])
    else:
        stack.append([a[i], stack[-1][1] + 1])
    
    if stack[-1][0] == stack[-1][1]:
        for _ in range(stack[-1][0]):
            stack.pop()
    #print(stack)
    print(len(stack) - 1)