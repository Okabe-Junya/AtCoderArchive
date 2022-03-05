a, b, c = map(int, input().split())
a_sum = (a*(a+1)) // 2
a_sum %= 998244353
b_sum = (b*(b+1)) // 2
b_sum %= 998244353
c_sum = (c*(c+1)) // 2
c_sum %= 998244353
print(a_sum * b_sum * c_sum % 998244353)
