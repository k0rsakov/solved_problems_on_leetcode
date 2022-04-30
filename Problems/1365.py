nums = [8,1,2,2,3]

smal_res = []
for i in nums:
    counter = 0
    for j in nums:
        if j < i:
            counter += 1
    smal_res.append(counter)


print(smal_res)