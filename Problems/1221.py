s = "RLRRLLRLRL"
n = ''
counter = 0
for i in s:
    n+=i
    c_R = n.count('R')
    c_L = n.count('L')
    if c_R == c_L:
        counter+=1

print(counter)