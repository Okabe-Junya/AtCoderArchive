string = input()
slist = list(string)
if slist[-1] == 's':
    string = string + 'es'
else:
    string = string + 's'
print(string)
