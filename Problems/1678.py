command = "G()()()()(al)"



str1 = ''
for i in range(len(command)):
    if command[i] == 'G':
        str1+=command[i]
    if command[i] == '(':
        if command[i+1] == ')':
            str1 += 'o'
        else:
            str1 += 'al'

print(str1)
