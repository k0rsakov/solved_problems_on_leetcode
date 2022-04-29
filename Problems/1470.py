nums = [2,5,1,3,4,7]
n = 3
res_nums = []
for i in range(0,n):
    res_nums.append(nums[i])
    res_nums.append(nums[i+n])

print(res_nums)