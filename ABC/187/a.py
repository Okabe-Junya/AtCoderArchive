a, b = map(int, input().split())
result_a = sum(list(map(int, str(a))))
result_b = sum(list(map(int, str(b))))
if result_a >= result_b:
    print(result_a)
else:
    print(result_b)
