v, t, s, d = map(int, input().split())
if not v * t <= d <= v * s:
    print('Yes')
else:
    print('No')
