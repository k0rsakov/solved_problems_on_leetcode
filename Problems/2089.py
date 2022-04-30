nums = [1,2,5,2,3]
target = 3
nums.sort()
res = []

for i in range(0, len(nums)):
    if nums[i] == target:
        res.append(i)
print(res)
