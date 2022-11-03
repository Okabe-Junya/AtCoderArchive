N = int(input())

three = N // 3
five = N // 5
seven = N // 7

three_five = N // 15
there_seven = N // 21
five_seven = N // 35

three_five_seven = N // 105

print(three + five + seven - three_five - there_seven - five_seven + three_five_seven)
