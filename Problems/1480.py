nums = [1,2,3,4]

nums_sum = [nums[0]]

for i in range(1,len(nums)):
    nums_sum.append(nums_sum[i-1]+nums[i])

print(nums_sum)