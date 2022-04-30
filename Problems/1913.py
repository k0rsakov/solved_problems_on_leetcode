nums = [4,2,5,9,7,4,8]


max1 = max(nums)
nums.pop(nums.index(max1))
max2 = max(nums)
nums.pop(nums.index(max2))
min1 = min(nums)
nums.pop(nums.index(min1))
min2 = min(nums)
nums.pop(nums.index(min2))

dif = (max1*max2)-(min1*min2)
print(dif)