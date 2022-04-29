num = 14
counter = 0
while num > 0:
    if num%2 == 0:
        num/=2
    else:
        num-=1
    counter+=1

print(counter)