accounts = [[2,8,7],[7,1,3],[1,9,5]]

max = 0

for i in accounts:
    if sum(i) > max:
        max = sum(i)

print(max)