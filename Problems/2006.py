nums = [1,2,2,1]
k = 1


counter, move = 0, 0
while move < len(nums):
    for i in range(move,len(nums)):
        if abs(nums[move]-nums[i]) == k:
            counter+=1
    move+=1
print(counter)

