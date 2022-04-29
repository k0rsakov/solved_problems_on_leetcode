operations = ["--X","X++","X++"]
n = 0
for i in operations:
    if i == '++X' or i == 'X++':
        n+=1
    else:
        n-=1


print(n)